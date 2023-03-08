const spawn = require("child_process").spawn;

let image_path='C:\\Users\\subek\\Desktop\\python-in-node\\images\\tree-736885__340.jpg'
let number_of_images=10

//  send parameters in the array after "./scriptName.py"
const pythonProcess = spawn("python.exe", ["./predict.py", image_path,number_of_images]);

pythonProcess.stdout.on("data", (data) => {
  console.log(data.toString());
});

pythonProcess.stderr.on("data", (data) => {
  console.error("error", data.toString());
});

pythonProcess.on("close", (code) => {
  console.log("process exited with code: ", code);
});
