CANVAS_COMPONENT = {
  "Canvas": {"description": "提供画布组件，用于自定义绘制图形，不支持子组件。"},
  "CanvasGradient": {"description": "渐变对象。"},
  "CanvasPattern": {"description": "一个Object对象，使用createPattern方法创建，通过指定图像和重复方式创建图片填充的模板。"},
  "CanvasRenderingContext2D": {"description": "使用RenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。"},
  "DrawingRenderingContext": {"description": "使用DrawingRenderingContext在Canvas组件上进行绘制，绘制对象可以是矩形、文本、图片等。"},
  "ImageBitmap": {"description": "ImageBitmap对象可以存储canvas渲染的像素数据。"},
  "ImageData": {"description": "ImageData对象可以存储canvas渲染的像素数据。"},
  "Matrix2D": {"description": "矩阵对象，可以对矩阵进行缩放、旋转、平移等变换。"},
  "OffscreenCanvas": {
    "description": "OffscreenCanvas组件用于自定义绘制图形。使用Canvas组件或Canvas API时，渲染、动画和用户交互通常发生在应用程序的主线程上，与画布动画和渲染相关的计算可能会影响应用程序性能。OffscreenCanvas提供了一个可以在屏幕外渲染的画布，这样可以在单独的线程中运行一些任务，从而避免影响应用程序主线程性能。"
  },
  "OffscreenCanvasRenderingContext2D": {
    "description": "使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是矩形、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到canvas上，加快了绘制速度。"
  },
  "Path2D": {"description": "路径对象，支持通过对象的接口进行路径的描述，并通过Canvas的stroke接口或者fill接口进行绘制。"}
}