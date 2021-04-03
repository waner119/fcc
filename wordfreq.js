var text = "I I am am am yes yes.";
// var text = $("#textarea").val();

function descend(x, y) {
  return x.count < y.count ? 1 : -1;
}

function wordFreq(text) {
  // 分词
  var splitText = text.split(/[ .?!,*'"]/);
  var wordArray = [];

  // 遍历 splitText，查询目标词
  splitText.forEach(function (target) {
    // 查询 wordArray 中是否含有目标词
    wordObj = wordArray.filter(function (w) {
      return w.word == target;
    });
    // 若有，计数+1
    if (wordObj.length) {
      wordObj[0].count += 1;
      // 若没有，添加
    } else {
      wordArray.push({ word: target, count: 1 });
    }
  });
  return wordArray.sort(descend);
}

console.log(wordFreq(text));

// document.getElementById("result").innerHTML = wordFreq(text);
