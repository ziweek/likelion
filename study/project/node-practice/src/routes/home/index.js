"use strict";

const express = require("express");
const router = express.Router();

const ctrl = require("./home.ctrl");

// 메소드 정의
router.get("/", ctrl.output.home);


module.exports = router;