"use strict";

const output = {
    home: (req, res) => {
        res.render("home/index");
    },
}

const input ={}

module.exports = {
    output,
    input
}