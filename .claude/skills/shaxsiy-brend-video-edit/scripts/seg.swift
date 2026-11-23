import Foundation
import Vision
import CoreImage

let args = CommandLine.arguments
let inDir = args[1], outDir = args[2]
let files = try FileManager.default.contentsOfDirectory(atPath: inDir).filter { $0.hasSuffix(".jpg") }.sorted()
let ctx = CIContext()
var n = 0
for f in files {
    let url = URL(fileURLWithPath: inDir).appendingPathComponent(f)
    guard let src = CIImage(contentsOf: url) else { continue }
    let req = VNGeneratePersonSegmentationRequest()
    req.qualityLevel = .accurate
    req.outputPixelFormat = kCVPixelFormatType_OneComponent8
    let handler = VNImageRequestHandler(ciImage: src, options: [:])
    try handler.perform([req])
    guard let obs = req.results?.first else { continue }
    var mask = CIImage(cvPixelBuffer: obs.pixelBuffer)
    let sx = src.extent.width / mask.extent.width, sy = src.extent.height / mask.extent.height
    mask = mask.transformed(by: CGAffineTransform(scaleX: sx, y: sy))
    mask = mask.applyingGaussianBlur(sigma: 1.5).cropped(to: src.extent)
    let outURL = URL(fileURLWithPath: outDir).appendingPathComponent(f.replacingOccurrences(of: ".jpg", with: ".png"))
    let cs = CGColorSpace(name: CGColorSpace.sRGB)!
    try ctx.writePNGRepresentation(of: mask, to: outURL, format: .RGBA8, colorSpace: cs, options: [:])
    n += 1
}
print("done \(n)")
