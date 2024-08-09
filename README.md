For years, I'd been doing this by hand - I'm sometimes not smart. My gf would agree.

This is a small script for joining images together (coins in my case) that have been provided of a uniform size and standardized naming convention.
It indexes all the images (jpg's) in the current folder, then uses the name and width/height of each odd image (1, 3, 5, 7, etc) to create a new image (double width) and pastes images i and i+1 into it and saves it, then moves onto the next pair.

If you've got "coin1.obv.jpg", "coin1.rev.jpg", "coin2.obv.jpg", "coin2.rev.jpg"
It'll create an array:
[0] coin1.obv.jpg
[1] coin1.rev.jpg
[2] coin2.obv.jpg
[3] coin2.rev.jpg

Then create "coin1.jpg" with coin1's height and 2*width
Then paste coin1.obv.jpg into it, followed by coin1.rev.jpg (offset by coin1.obv.jpg's width)
and save it as a new double width image with both the front and back images
