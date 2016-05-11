ffmpeg -i input_video.mp4 -ss 00:00:30 -t 00:00:10 -c:a copy -c:v copy cropped.mp4
convert -depth 8 -background none plate.svg -resize 50% plate.PNG
ffmpeg -i cropped.mp4 -i plate.png -filter_complex "[0:v][1:v]overlay=x=0:y=446:enable='between(t,1,9)'" -c:a copy  plated.mp4
ffmpeg -i plated.mp4 -filter_complex  "[0:v]drawtext=fontfile=arial.ttf:fontcolor=black@1.00:fontsize=14:text='Victoria':x=200:y=476:enable='between(t,2,9)'" -c:a copy result.mp4

