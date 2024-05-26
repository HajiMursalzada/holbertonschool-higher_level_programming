document.addEventListener("DOMContentLoaded", () => {
  const helloElement = document.getElementById("hello");

  fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
    .then((response) => response.json())
    .then((data) => {
      const translation = data.hello;
      helloElement.textContent = translation;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
