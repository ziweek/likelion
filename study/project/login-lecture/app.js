"use strict";

// 모듈
const express = require("express");
const bodyParser = require("body-parser");
const app = express();

//라우팅
const home = require("./src/routes/home");

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
// 앱 세팅
app.set("views", "./src/views");
app.set("view engine", "ejs");
app.use("/", home);
app.use(express.static(`${__dirname}/src/public`));

module.exports = app;
