const express = require("express");
const app = express();


// MVC 중 V
app.set("views", "./src/views");
app.set("view engine", "ejs");


// MVC 중 C
const home = require("./src/routes/home");
app.use("/", home);


// app.get("/", (req, res) => {
//     res.send("Hello, world")
// });

// const PORT = 3000
// app.listen(PORT, () => {
//     console.log("서버 가동")
// })

module.exports = app;