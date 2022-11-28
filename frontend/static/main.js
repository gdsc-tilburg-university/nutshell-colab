var summaryContentElement = document.querySelector("#summaryContent");

const getSummaryContent = async () => {
  const response = await fetch("/summary_content");
  const textContentArray = await response.json();
  summaryContentElement.innerHTML = "";
  textContentArray.forEach((summaryBlock) => {
    try {
      var pElement = document.createElement("p");
      pElement.textContent = summaryBlock[0]["summary_text"];
      summaryContentElement.appendChild(pElement);
    } catch (e) {
      console.error(e);
    }
  });
};

var interval = window.setInterval(getSummaryContent, 1000);
