// Initialize butotn with users's prefered color
let btn = document.getElementById("open-btn");

async function getCurrentTab() {
  let queryOptions = { active: true, currentWindow: true };
  let [tab] = await chrome.tabs.query(queryOptions);
  tab.ur
  return tab;
}

// btn.addEventListener("click", async () => {
//   let tab = await getCurrentTab()
//   alert(tab.url)
// });
