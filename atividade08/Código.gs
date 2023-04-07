const htmlFile = "Blog.html";

function doGet(e) {
  if (e.parameter.message && e.parameter.author) {
    saveMessage(e.parameter.message, e.parameter.author);
  }
  return HtmlService.createTemplateFromFile(htmlFile).evaluate();
}

function saveMessage(message, author) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var timestamp = new Date();
  sheet.appendRow([author, message, timestamp]);
}

function getMessages() {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  var data = sheet.getDataRange().getValues();
  return JSON.stringify(data);
}
