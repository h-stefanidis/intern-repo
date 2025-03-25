const puppeteer = require('puppeteer');
const path = require('path');

(async () => {
  // Build a file URL for the calculator.html
  const filePath = 'file://' + path.resolve(__dirname, 'calculator.html');

  // Launch Puppeteer in headless mode (default)
  const browser = await puppeteer.launch({ headless: true });
  const page = await browser.newPage();
  
  // Navigate to the calculator page
  await page.goto(filePath);

  // Enter values into the input fields
  await page.type('#num1', '5');
  await page.type('#num2', '3');

  // Click the "Add" button
  await page.click('#addButton');
  
  // Wait for the result to be updated
  await page.waitForSelector('#result');
  const result = await page.$eval('#result', el => el.innerText);

  console.log('Result:', result);

  // Check if the result is as expected (5 + 3 should equal 8)
  if (result === '8') {
    console.log('Test Passed');
  } else {
    console.log('Test Failed');
    process.exit(1);
  }

  await browser.close();
})();
