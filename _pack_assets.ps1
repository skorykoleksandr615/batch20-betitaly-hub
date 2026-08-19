Add-Type -AssemblyName System.Drawing
$srcRoot = Join-Path $env:USERPROFILE ".cursor\projects\c-AndroidStudioProjects-batch20-hubs\assets"
$dstRoot = "C:\AndroidStudioProjects\batch20-hubs\betitaly"
$map = @{
  "bi-logo.png" = "assets\brand\logo.png"
  "bi-hero.jpg" = "assets\hero.jpg"
  "bi-og.jpg" = "assets\og.jpg"
  "bi-slot-dog-house.jpg" = "assets\slots\the-dog-house.jpg"
  "bi-slot-wolf-gold.jpg" = "assets\slots\wolf-gold.jpg"
  "bi-slot-canyon-gold.jpg" = "assets\slots\wild-west-gold.jpg"
  "bi-slot-great-rhino.jpg" = "assets\slots\great-rhino.jpg"
  "bi-slot-buffalo-king.jpg" = "assets\slots\buffalo-king.jpg"
  "bi-slot-cleopatra.jpg" = "assets\slots\cleopatra.jpg"
  "bi-slot-fruit-party.jpg" = "assets\slots\fruit-party.jpg"
  "bi-slot-bbb.jpg" = "assets\slots\big-bass-bonanza.jpg"
  "bi-slot-wisdom-athena.jpg" = "assets\slots\wisdom-of-athena.jpg"
  "bi-slot-starlight.jpg" = "assets\slots\starlight-princess.jpg"
  "bi-crash-jetx.jpg" = "assets\crash\jetx.jpg"
  "bi-crash-aviator.jpg" = "assets\crash\aviator.jpg"
  "bi-crash-plinko.jpg" = "assets\crash\plinko.jpg"
  "bi-crash-spaceman.jpg" = "assets\crash\spaceman.jpg"
  "bi-crash-lucky-jet.jpg" = "assets\crash\lucky-jet.jpg"
  "bi-crash-mines.jpg" = "assets\crash\mines.jpg"
  "bi-live-lightning.jpg" = "assets\live\lightning-roulette.jpg"
  "bi-live-crazy-time.jpg" = "assets\live\crazy-time.jpg"
  "bi-live-blackjack.jpg" = "assets\live\blackjack.jpg"
  "bi-live-mega-wheel.jpg" = "assets\live\mega-wheel.jpg"
  "bi-live-baccarat.jpg" = "assets\live\baccarat.jpg"
  "bi-live-dream-catcher.jpg" = "assets\live\dream-catcher.jpg"
  "bi-page-login.jpg" = "assets\pages\bi-login.jpg"
  "bi-page-join.jpg" = "assets\pages\bi-join.jpg"
  "bi-page-bonus.jpg" = "assets\pages\bi-bonus.jpg"
  "bi-page-slots.jpg" = "assets\pages\bi-slots.jpg"
  "bi-page-odds.jpg" = "assets\pages\bi-odds.jpg"
  "bi-page-crash.jpg" = "assets\pages\bi-crash.jpg"
  "bi-page-live.jpg" = "assets\pages\bi-live.jpg"
  "bi-page-app.jpg" = "assets\pages\bi-app.jpg"
  "bi-page-pay.jpg" = "assets\pages\bi-pay.jpg"
  "bi-page-help.jpg" = "assets\pages\bi-help.jpg"
  "bi-promo-bonus.jpg" = "assets\promo\promo-bonus.jpg"
  "bi-promo-slots.jpg" = "assets\promo\promo-slots.jpg"
  "bi-promo-crash.jpg" = "assets\promo\promo-crash.jpg"
  "bi-promo-live.jpg" = "assets\promo\promo-live.jpg"
  "bi-promo-odds.jpg" = "assets\promo\promo-odds.jpg"
  "bi-promo-pay.jpg" = "assets\promo\promo-pay.jpg"
  "bi-promo-login.jpg" = "assets\promo\promo-login.jpg"
  "bi-promo-join.jpg" = "assets\promo\promo-join.jpg"
  "bi-promo-app.jpg" = "assets\promo\promo-app.jpg"
  "bi-promo-help.jpg" = "assets\promo\promo-help.jpg"
}

function Save-Jpeg($img, $path, $quality) {
  $codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq "image/jpeg" }
  $ep = New-Object System.Drawing.Imaging.EncoderParameters(1)
  $ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]$quality)
  $img.Save($path, $codec, $ep)
}

function Fit-Copy($srcImg, $maxW) {
  if ($srcImg.Width -le $maxW) { return $srcImg }
  $nh = [int]($srcImg.Height * $maxW / $srcImg.Width)
  $bmp = New-Object System.Drawing.Bitmap $maxW, $nh
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.DrawImage($srcImg, 0, 0, $maxW, $nh)
  $g.Dispose()
  return $bmp
}

foreach ($k in $map.Keys) {
  $src = Join-Path $srcRoot $k
  $dst = Join-Path $dstRoot $map[$k]
  $dir = Split-Path $dst -Parent
  if (-not (Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  if (-not (Test-Path $src)) { Write-Output "MISSING $k"; continue }
  $img = [System.Drawing.Image]::FromFile($src)
  if ($k -like "*.png") {
    $max = 512
    $side = [Math]::Max($img.Width, $img.Height)
    $scale = if ($side -gt $max) { $max / $side } else { 1 }
    $nw = [Math]::Max(1, [int]($img.Width * $scale))
    $nh = [Math]::Max(1, [int]($img.Height * $scale))
    $bmp = New-Object System.Drawing.Bitmap $nw, $nh
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.Clear([System.Drawing.Color]::FromArgb(7,20,40))
    $g.DrawImage($img, 0, 0, $nw, $nh)
    $g.Dispose()
    $bmp.Save($dst, [System.Drawing.Imaging.ImageFormat]::Png)
    $bmp.Dispose()
  } else {
    $maxW = if ($map[$k] -match "promo|og.jpg") { 1600 } else { 1200 }
    $fitted = Fit-Copy $img $maxW
    Save-Jpeg $fitted $dst 82
    if ($fitted -ne $img) { $fitted.Dispose() }
  }
  $img.Dispose()
  $len = (Get-Item $dst).Length
  Write-Output ("{0}`t{1}" -f $map[$k], $len)
}

$logoPath = Join-Path $dstRoot "assets\brand\logo.png"
$logo = [System.Drawing.Image]::FromFile($logoPath)
$sizes = @{
  "favicon-32x32.png" = 32
  "favicon-48x48.png" = 48
  "favicon-96x96.png" = 96
  "favicon-192x192.png" = 192
  "apple-touch-icon.png" = 180
}
foreach ($name in $sizes.Keys) {
  $sz = $sizes[$name]
  $bmp = New-Object System.Drawing.Bitmap $sz, $sz
  $g = [System.Drawing.Graphics]::FromImage($bmp)
  $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $g.Clear([System.Drawing.Color]::FromArgb(7,20,40))
  $g.DrawImage($logo, 0, 0, $sz, $sz)
  $g.Dispose()
  $out = Join-Path $dstRoot $name
  $bmp.Save($out, [System.Drawing.Imaging.ImageFormat]::Png)
  $bmp.Dispose()
  Write-Output ("{0}`t{1}" -f $name, (Get-Item $out).Length)
}
$ico32 = Join-Path $dstRoot "favicon-32x32.png"
Copy-Item $ico32 (Join-Path $dstRoot "favicon.ico") -Force
Write-Output ("favicon.ico`t{0}" -f (Get-Item (Join-Path $dstRoot "favicon.ico")).Length)
$logo.Dispose()
Write-Output "OK"
