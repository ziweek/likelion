function buySomething(nowMoney) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const pay = parseInt(prompt("금액 입력"));
      const remain = nowMoney - pay;
      if (remain >= 0) {
        console.log(`${pay}원 지불`);
        resolve(remain);
      } else {
        reject(`잔액부족: 현재 잔액${nowMoney}원`);
      }
    }, 2000);
  });
}

buySomething(1000)
  .then((res) => {
    console.log(res);
    buySomething(res).then((res) => {
      console.log(res);
      buySomething(res).then((res) => {
        console.log(res);
        buySomething(res);
      });
    });
  })
  .catch((err) => console.log(err));
