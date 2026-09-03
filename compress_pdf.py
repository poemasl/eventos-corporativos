#!/usr/bin/env python3
import sys
import Quartz
from Foundation import NSURL

def compress(src, dst, filter_path):
    src_url = NSURL.fileURLWithPath_(src)
    doc = Quartz.CGPDFDocumentCreateWithURL(src_url)
    if not doc:
        print("No se pudo abrir", src); return
    dst_url = NSURL.fileURLWithPath_(dst)
    filt = Quartz.QuartzFilter.quartzFilterWithURL_(NSURL.fileURLWithPath_(filter_path))
    ctx_opts = {"QuartzFilter": filt}
    writeCtx = Quartz.CGPDFContextCreateWithURL(dst_url, None, ctx_opts)
    n = Quartz.CGPDFDocumentGetNumberOfPages(doc)
    for i in range(1, n + 1):
        page = Quartz.CGPDFDocumentGetPage(doc, i)
        rect = Quartz.CGPDFPageGetBoxRect(page, Quartz.kCGPDFMediaBox)
        Quartz.CGContextBeginPage(writeCtx, rect)
        Quartz.CGContextDrawPDFPage(writeCtx, page)
        Quartz.CGContextEndPage(writeCtx)
    Quartz.CGPDFContextClose(writeCtx)
    print("Comprimido:", dst)

if __name__ == "__main__":
    filter_path = "/System/Library/Filters/Reduce File Size.qfilter"
    compress(sys.argv[1], sys.argv[2], filter_path)
