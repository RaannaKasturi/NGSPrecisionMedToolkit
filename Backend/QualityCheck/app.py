from main import main
import gradio as gr

def get_fastq(accession, alignment_filter_type, alignment_filter, compressed, skip_technical, remove_adapter, spot_group, min_reads, max_reads, ar_specific, ar_start, ar_end, member):
    print("accession: ", accession)
    print("alignment_filter_type: ", alignment_filter_type)
    print("alignment_filter: ", alignment_filter)
    print("compressed: ", compressed)
    print("skip_technical: ", skip_technical)
    print("remove_adapter: ", remove_adapter)
    print("spot_group: ", spot_group)
    print("min_reads: ", min_reads)
    print("max_reads: ", max_reads)
    print("ar_specific: ", ar_specific)
    print("ar_start: ", ar_start)
    print("ar_end: ", ar_end)
    print("member: ", member)
    data, download_status, files = main(accession, alignment_filter_type, alignment_filter, compressed, skip_technical, remove_adapter, spot_group, min_reads, max_reads, ar_specific, ar_start, ar_end, member)
    return data, download_status, files

def enable_spot_group(esg):
    if esg == True:
        return gr.update(visible=True)
    else:
        return gr.update(visible=False)

def enable_reads_count(erc):
    if erc == True:
        return gr.update(visible=True), gr.update(visible=True)
    else:
        return gr.update(visible=False), gr.update(visible=False)
    
def enable_alignment_filter(eaf):
    if eaf == True:
        return gr.update(visible=True)
    else:
        return gr.update(visible=False)

def enable_alignment_filter_type(eaft):
    if eaft == "aligned-region":
        return gr.update(visible=True), gr.update(visible=True), gr.update(visible=True)
    elif eaft == "matepair-distance":
        return gr.update(visible=False), gr.update(visible=True), gr.update(visible=True)
    else:
        return gr.update(visible=False), gr.update(visible=False), gr.update(visible=False)

def app():
    with gr.Blocks(title="SRA Downloader") as webui:
        with gr.Row():
            with gr.Column():
                accession = gr.Textbox(label="Enter SRA Number", placeholder="ERR11468775", type="text", interactive=True)
                with gr.Column():
                    compression = gr.Checkbox(label="Compress")
                    skip_technical = gr.Checkbox(label="Skip Technical details")
                    remove_adapter = gr.Checkbox(label="Remove Adapter")
                    spot_group = gr.Checkbox(label="Enable Spot Grouping")
                    member = gr.Textbox(label="Member", placeholder="Enter Member", type="text", interactive=True, visible=False)
            with gr.Column():
                apply_min_max_reads = gr.Checkbox(label="Enable Min & Max Reads Count")
                min_reads = gr.Number(label="Minimum Reads", visible=False)
                max_reads = gr.Number(label="Maximum Reads", visible=False)
            with gr.Column():
                alignment_filter = gr.Checkbox(label="Apply Alignment Filters")
                alignment_filter_type = gr.Radio(label="Alignment Filter Type", choices=["split-spot", "aligned", "unaligned", "aligned-region", "matepair-distance"], visible=False)
            with gr.Column():
                ar_specific = gr.Textbox(label="Aligned Region Specific", placeholder="Enter Specific Region", type="text", interactive=True, visible=False)
                ar_start = gr.Number(label="Aligned Region Start", visible=False)
                ar_end = gr.Number(label="Aligned Region End", visible=False)
            apply_min_max_reads.change(fn=enable_reads_count, inputs=apply_min_max_reads, outputs=[min_reads, max_reads])
            alignment_filter.change(fn=enable_alignment_filter, inputs=alignment_filter, outputs=[alignment_filter_type])
            alignment_filter_type.change(fn=enable_alignment_filter_type, inputs=alignment_filter_type, outputs=[ar_specific, ar_start, ar_end])
            spot_group.change(fn=enable_spot_group, inputs=spot_group, outputs=[member])
            btn2 = gr.Button(value="Download SRA Data")
        with gr.Row():
            data = gr.Textbox(label="Data", placeholder="Data", lines=10, type="text", interactive=True)
            download_status = gr.Textbox(label="Download Status", placeholder="Download Status", lines=5,type="text", interactive=True)
            files = gr.File(label="Download your File")
        btn2.click(get_fastq,
                   inputs= [accession, alignment_filter_type, alignment_filter, compression, skip_technical, remove_adapter, spot_group, min_reads, max_reads, ar_specific, ar_start, ar_end, member],
                   outputs=[data, download_status, files])
    try:
        webui.queue(default_concurrency_limit=25).launch()
    except Exception as e:
        print(f"Error: {e}")


app()