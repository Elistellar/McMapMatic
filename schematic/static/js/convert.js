function updateImage(input, id) {
    if (input.files && input.files[0]) {
        var reader = new FileReader()

        reader.onload = function (e) {

            var img = document.getElementById(id)

            img.src = e.target.result
            img.style.height = "256px"
            img.style.width = "256px"
        }

        reader.readAsDataURL(input.files[0])
    }
}

function setImg(input) {
    const colorId = input.name.split("_")[1]
    var colorImg = document.getElementById(`img-${colorId}`)
    var blockImg = input.nextElementSibling
    colorImg.src = blockImg.src
}