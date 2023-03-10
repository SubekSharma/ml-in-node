const spawn = require("child_process").spawn;

let image_path = 'https://cdn.britannica.com/55/174255-050-526314B6/brown-Guernsey-cow.jpg?w=400&h=300&c=crop'
let number_of_tags = 10

const pythonProcess = spawn("python.exe", ["./classify.py", image_path, number_of_tags]);

pythonProcess.stdout.on("data", (data) => {
  console.log(data.toString());
});

pythonProcess.stderr.on("data", (data) => {
  console.error("error", data.toString());
});

pythonProcess.on("close", (code) => {
  console.log("process exited with code: ", code);
});
