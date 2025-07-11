async function generateImage() {
  const prompt = document.getElementById('inputPrompt').value;
  const output = document.getElementById('imageOutput');
  output.innerHTML = 'Generating image...';

  try {
    const response = await fetch("http://127.0.0.1:5000/generate-image", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt: prompt })
    });

    const data = await response.json();
    if (data.error) {
      output.innerHTML = "❌ Error: " + data.error;
    } else {
      output.innerHTML = `<img src="${data.url}" alt="Generated Image"/>`;
    }
  } catch (err) {
    output.innerHTML = "❌ Network Error";
  }
}
