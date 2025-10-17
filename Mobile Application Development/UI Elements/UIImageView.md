Setting images
- Create a file to hold the images under the asset folder of your project. 

```swift
var imageChoice: UIImageView!

// Setup
func setupImage() {
	imageChoice = UIImageView()
	imageChoice.image = UIImage(systemName: "photo")
	imageChoice.contentMode = .scaleToFill
	imageChoice.layer.cornerRadius = 10
	imageChoice.translatesAutoresizingMaskIntoConstrants = false
	warpperCellView.addSubview(imageChoice)
}

func initCosntraints() {
	NSLayoutCosntraint.activate([
		// MARK: Set constraints normall
		// Set height and width with constraints
		imageChoice.heightAnchor.constraint(equalTo: <element>.heightAnchor, constant: -<margin>)
		imageChoice.widthAnchor.constraint(equalTo: <element>.heightAnchor, constant: -<margin>)
		
		
	])
}
```