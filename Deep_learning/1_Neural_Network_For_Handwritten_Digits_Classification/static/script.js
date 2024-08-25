const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let isDrawing = false;

// Initialize the canvas and set up drawing events
canvas.addEventListener("mousedown", (e) => {
    isDrawing = true;
    ctx.moveTo(e.offsetX, e.offsetY);
});

canvas.addEventListener("mousemove", (e) => {
    if (isDrawing) {
        ctx.lineTo(e.offsetX, e.offsetY);
        ctx.stroke();
    }
});

canvas.addEventListener("mouseup", () => {
    isDrawing = false;
});

canvas.addEventListener("mouseout", () => {
    isDrawing = false;
});

// Function to get the drawn image data and send it to the backend
async function predict() {
    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const data = imageData.data;
    const grayData = [];

    // Convert to grayscale
    for (let i = 0; i < data.length; i += 4) {
        const gray = (data[i] + data[i + 1] + data[i + 2]) / 3;
        grayData.push(gray);
    }

    // Reshape the data for the model
    const reshapedData = [];
    for (let i = 0; i < canvas.height; i++) {
        reshapedData.push(grayData.slice(i * canvas.width, (i + 1) * canvas.width));
    }

    // Send the data to the FastAPI backend
    const response = await fetch("/predict/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ data: reshapedData }),
    });

    const result = await response.json();
    document.getElementById("prediction-result").innerText = `Prediction: ${result.prediction}`;
}
