# JavaScript

JS是一种脚本语言，用于页面交互以及动态样式，适配于所有现在的浏览器。

## 杂

- 注释

  - `//`  单行注释
  - `/*  */` 多行注释
- 检验数据类型

  ```js
  typeof 3   // returns 'number'
  typeof '3' // returns 'string'
  ```

## JS 八种数据类型

### undefined 未定义

### null 空值

### boolean  布尔值

布尔值只有两个值，分别是 `true`和 `false`

**1. if 条件**

```js
/* 原理 */
if (condition is true) {
  statement is executed
}

/* 例子 */
function test (myCondition) {
  if (myCondition) {
     return "It was true";  // Return 这里面的命令需要满足myCondition是True
  }
  return "It was false";
}
test(true);  // if会检验这行括号里的值是否和myCondition匹配，如果匹配是True，returns "It was true"
test(false); // 如果不是，returns "It was false"

/* 实际例子 */
function testEqual(val) {
  if (val ==12) { 
    return "Equal";
  }
  return "Not Equal";
}

testEqual(12); //括号里的值与if后条件匹配，看是True还是Flase

/* 同时满足多个条件，用`&&`连接 */
function testLogicalAnd(val) {
  if (val <= 50 && val >= 25) {
      return "Yes";
    }
  return "No";
}

testLogicalAnd(10); //Returns No

/* 多个条件满足其一，用`||`连接 */
function testLogicalOr(val) {
  if (val >20 || val< 10) {
    return "Outside";
  }
  return "Inside";
}

testLogicalOr(15); // Returns Inside
```

**1.1 if else用法**

```js
if (num > 10) {
  return "Bigger than 10";
} else {
  return "10 or Less";
}

// 可在else后面加if给多个具体条件
if (num > 15) {
  return "Bigger than 15";
} else if (num < 5) {
  return "Smaller than 5";
} else if (num < 2) {
  return "Smaller than 2";
} else {
  return "Between 2 and 15";
}
```

**1.2 结果优先级**

代码是从上往下运行的，会优先运行行数在上的结果。

```js
function foo(x) {
  if (x < 1) {
    return "Less than one";
  } else if (x < 2) {
    return "Less than two";
  } else {
    return "Greater than or equal to two";
  }
}

function bar(x) {
  if (x < 2) {
    return "Less than two";
  } else if (x < 1) {
    return "Less than one";
  } else {
    return "Greater than or equal to two";
  }
}
/* 运行结果 */
foo(0) // "Less than one"
bar(0) // "Less than two"
```

**2. 不同数据对比**

`==` 相等，`!=` 不相等，`>`大于，`>=`大于等于，`<` 小于，`<=`小于等于，不同数据类型可以转换

`===` 严格相等，`!===` 严格不相等，数据类型需要一样

| 代码 | 对错 |
| - | - |
| 1   ==  1 | True |
| 1   ==  2 | False |
| 1   == '1' | True |
| "3" ==  3 | True |
| 3 ===  3 | True |
| 3 === '3' | False |

### string  字符串

### symbol 符号

### BigInt  比2<sup>53</sup> -1 大的数值

### number  数值

### object 对象

用于以结构化的方式储存数据，数据可以是真实世界的实物，例如猫。通常可以用属性 `properties` 来访问这个数据。

```js
var cat = {
  "name": "Whiskers",
  "legs": 4,
  "tails": 1,
  "enemies": ["Water", "Dogs"]  //一个property里两个值
};
/* name, leg 等就是property，这种是字符串，也可以是数字 */
var anotherObject = {
  make: "Ford",   // 单个词的字符串可以省略引号
  5: "five",
  "model": "focus"
};
```

**1. 访问对象property**

- 两种方式，`.` 和`[]`

```js
/* 圆点用于当你知道这个对象的property名字时 */
var myObj = {
  prop1: "val1",
  prop2: "val2"
};
var prop1val = myObj.prop1;
var prop2val = myObj.prop2;

/* []用于对象property名字里带有空格（引用时必须有引号），但也可以用于没有空格 */
var myObj = {
  "Space Name": "Kirk",
  "More Space": "Spock",
  "NoSpace": "USS Enterprise"
};
myObj["Space Name"];
myObj['More Space'];
myObj["NoSpace"];

/* 使用变量访问 */
var dogs = {
  Fido: "Mutt",  Hunter: "Doberman",  Snoopie: "Beagle"
};
var myDog = "Hunter";
var myBreed = dogs[myDog];  
console.log(myBreed);  // 输出字符串Doberman

```

**2. 更改property的值**

```js
var myDog = {
  "name": "Coder",
  "legs": 4,
  "tails": 1,
  "friends": ["freeCodeCamp Campers"]
};

myDog.name = "Happy Coder";  // Coder 被改成了Happy Coder
myDog["name"] = "Happy Coder"; // 这个跟上面的都可以
```

**3. 增减property**

```js
var ourDog = {
  "name": "Camper",
  "legs": 4,
  "tails": 1,
  "friends": ["everything!"]
};

ourDog.bark = "bow-wow";  // 新增属性
delete ourDog.friends; // 减去属性
```

## 句法

乱七八糟各种句法

### 1. 多重选择

`switch`

是一种条件语句，跟 `if` `else` 有些相似。针对多种可能的情况评估表达式，并根据匹配的情况执行代码块。

- `case` 后面的值匹配的时候需要绝对相等`===`
- `break` 是告诉JS此句已终止，如果没有`break`，会执行下一句
- 比`ifelse` 写起来要简洁

```js
function caseInSwitch(val) {
  var answer = "";
switch(val) {
  case 1:
    return "alpha";
    break;
  case 2:
    return "beta";
    break;
  case 3:
    return "gamma";
    break;
  case 4:
    return "delta";
    break;
  default:   //相当于`if`语句中的最后一个`else`
    return "letter"
    break
}
  return answer;
}

caseInSwitch(1);
```

**3.1 多个值一个输出**

```js
function sequentialSizes(val) {
  var answer = "";
 switch(val) {
   case 1:   //三个值一个输出`low`
   case 2:
   case 3:
    return "Low"
    break
   case 4:
   case 5:
   case 6:
    return "Mid"
    break  
 }
  return answer;
}

sequentialSizes(1);
```

## 赋值

`variable`

命名可用数字，字母，`$`, `_` 命名，不可包含空格或用数字开头，命名区分大小写。建议的命名方式 `camelCase`，即第一个单词首字母小写，之后的单词首字母皆大写。

```js
var myVar;
myVar = 5;
```

### 1. 储存多个值

array   可以储存多个数据类型，用逗号隔开

```js
//单个方括号
var myArray = ["Katelyn", 25];
//多个方括号, 括号内外都要逗号隔开
var myArray = [["Katelyn", 25], ["Kate", 30]];
```

**1.1 多值内索引**

`变量名[N]`  从0开始

```js
/* 单行值索引  */
var array = [50,60,70];
array[0]; // equals 50
var data = array[1];  // equals 60

/* 多行值索引，叫multi-dimension array  */
var arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
  [[10,11,12], 13, 14]
];
arr[3]; // equals [[10,11,12], 13, 14]
arr[3][0]; // equals [10,11,12]
arr[3][0][1]; // equals 11
```

**1.2 修改变量里的值**

`变量名[N] =`

```js
var ourArray = [50,40,30];
ourArray[0] = 15; // equals [15,40,30]
```

**1.3 多值变量开始及结尾加值**

`.unshift()` 开始

`.push()` 结尾

```js
/* 开始 */
var ourArray = ["Stimpson", "J", "cat"];
ourArray.shift(); // ourArray now equals ["J", "cat"]
ourArray.unshift("Happy");
// ourArray now equals ["Happy", "J", "cat"]

/* 结尾 */
var arr1 = [1,2,3];
arr1.push(4);
// arr1 is now [1,2,3,4]

var arr2 = ["Stimpson", "J", "cat"];
arr2.push(["happy", "joy"]);
// arr2 now equals ["Stimpson", "J", "cat", ["happy", "joy"]
```

**1.4 消除首值和尾值**

`.shift()` 消除首值，新变量=消除的值，原变量=消除后的值

`.pop()`   消除尾值

```js
var threeArr = [1, 4, 6];
var oneDown = threeArr.pop();  //消除了6，并在下一行oneDown变量返还了该值
console.log(oneDown); // Returns 6
console.log(threeArr); // Returns [1, 4], 被.pop消除了结尾值6
```

### 乱 赋值

**1. Shopping List**

变量   `myList`

一个list至少有五组值，每一组由一个字符串和一个数值组成。

```js
var myList = [
    ["Chocolate Bar", 15], ["Milk",1], ["Bread", 1], ["Pear", 1], ["Stawberry", 2]];
```

### 数据类型赋值

八种数据类型可能会被储存在变量里。

| 数据类型 | 解释 | 例子 |
| - | - | - |
| `string` | 字符串，需要引号括起来 | `let myVariable = 'Bob';` |
| `number` | 数字，不需要引号 | `let myVariable = 10;` |
| `boolean` | 布尔值，True/False value，不需要引号 | `let myVariable = true;` |
| `array` | 数据组，可以储存多个值 | `let myVariable = [1,'Bob','Steve',10];` |
| `object` | 可以是任何东西 | `let myVariable = document.querySelector('h1');` |

#### 数值赋值

**1. 赋值初始值**

```js
var myVar = 0;
//可用 `+`  `-` `*` `/` 计算，支持小数及小数运算。
var sum = 10 + 10;
var difference = 45 - 33;
var product = 8 * 10;
var quotient = 66 / 33;
```

**2. 快捷运算**

| 代码 | 意思 |   |
| - | - | - |
| `i++;` | `i = i + 1;` |   |
| `i--;` | `i = i - 1;` |   |
|   |   |   |

**3. 运算符号**

| 符号 | 运算方式 | 例子 | 备注 |
| - | - | - | - |
| % | 余数 | `17 % 2` = 1 | 不适宜用在负数上 |
|   |   |   |   |
|   |   |   |   |

> 17 - 2\*2*2\*2 = 1

**4. 加减乘除复合赋值**

```

```

`+=`   `-=`   `*=`   `/=`

```js
// 加法
var myVar = 1;
myVar += 5;
console.log(myVar); // Returns 6
// 乘法 a*=5 等于 a = a*5
var a = 5;
a *= 5;
console.log(a); // Returns 25
```

#### 字符串赋值

字符串一旦创立，其他元素无法改变，但可以自身改变。

```js
var myFirstName = "Katelyn"
var myLastName = "Lee"
```

**1. 转义字符 escape character**

- 使用目的

  - 打出你打不出的元素，例如回车
  - 引号重复，避免字符串提前结束
- 不同转义字符的意思

| 字符 | 意思 | 备注 |
| - | - | - |
| `\'` | 单引号 |   |
| `\"` | 双引号 |   |
| `\n` | 新的一行 |   |
| `\r` | 回车 |   |
| `\t` | tab |   |
| `\b` | word boundary |   |
| `\f` | form feed |   |

**2. 字符串连接**

```js
// 用`+`号
var ourStr = "I come first. " + "I come second."; 
//用`+=`号
var ourStr = "I come first. ";
ourStr += "I come second.";
/* 两个都Returns "I come first. I come second." */

//句子和变量连接
var myName = "Katelyn";
var myStr = "My name is " + myName + ", and I am well.";
/* Returns "My name is Katelyn, and I am well." */

//变量和变量连接 `+=`
var anAdjective = "awesome!";
var ourStr = "freeCodeCamp is ";
ourStr += anAdjective;
/* Returns "freeCodeCamp is awesome!" */
```

> 注意空格，需要自己加空格。

**3. 计算字符串长度**

`变量名.length`

```js
var lastNameLength = 0;
var lastName = "Lovelace";
lastNameLength = lastName.length;
```

**4. 变量字符索引**

`变量名[N]`

正数字符索引。数字是从0开始，第一个character实际上是0.

```js
var firstLetterOfLastName = "";
var lastName = "Lovelace";

firstLetterOfLastName = lastName[0]; 
// Returns "L"
```

`变量名[变量名.length - N]`

倒数字符索引。倒数第几位，N就是几。

```js
var firstName = "Charles";
var lastLetter = firstName[firstName.length - 1]; 
// Returns "s"
```

**5. 赋值改变**

```js
var myStr = "Bob";
myStr = "Job";
```

#### 布尔值赋值

## 函数

`function`

```js
function reusableFunction() {
  console.log("Hi World");
}
reusableFunction();  //使用这个会运行{}里的所有代码

/* 一个函数运行完的标志是return输出 */
function myFun() {
  console.log("Hello");
  return "World";       // 运行到这里，后面的不会运行
  console.log("byebye")
}
myFun();

```

**1. 函数里的参数 argument**

创建两个当占位符的参数，在赋予值 (*arguments*)

- 占位符可以是数据类型的缩写，例如`arr`,`num`,`item`,`str`等

```Js
function functionWithArgs(one, two) { // one和two是当占位符的参数
  console.log(one+two); // 中间要有 + 号
}
functionWithArgs(6, 16);  // 赋予两个值，一个6，一个16
```

**2. 作用域 scope**

- 在`function`外的变量，JS随处可见，称为*Global scope*
- 在`function`内的变量，只有在那个`function`里才能见，称为*local scope*

```js
/* function内的变量 */
function myTest() {
  var loc = "foo";
  console.log(loc);
}
myTest(); // logs "foo"
console.log(loc); // loc is undefined
```

- **优先级**

`local`  比 `global`优先级高

```js
var someVar = "Hat";  // Global variable
function myFun() {
  var someVar = "Head"; // Local variable
  return someVar; // Returns "Head"
}
```

**3. 返回值**

`return`

```js
function plusThree(num) {
  return num + 3;
}
var answer = plusThree(5); // Returns 8

/* 返回值赋值 */
var processed = 0;
function processArg(num) {
  return (num + 3) / 5;
}

processed = processArg(7); // 此行，用返回值赋值
```

**4. 一连串的值 line**

`arr`是数组，`item`是数值

```js
function nextInLine(arr, item) {
arr.push(item); //给nextInLine函数数组arr最后增加一个数字值
 var removed = arr.shift(); // 删除函数数组第一个值
 return removed;  // 返还被删除的第一个值
}

// Setup
var testArr = [1,2,3,4,5];

// Display code
console.log("Before: " + JSON.stringify(testArr));
console.log(nextInLine(testArr, 6));
console.log("After: " + JSON.stringify(testArr));
```

**5. 对比大小**

```js
function isLess(a, b) {
  return a < b;
}

isLess(10, 15);  //return true
isLess(15, 10);  // return false
```

## Q&A

1. 函数需要return，return后answer才有函数结果。
2. `console log` 是给网页控制台输出信息的，类似`print`.  弹窗为`alert`.
3.

## 专业词汇

| 单词 | 意思 | 备注 |
| - | - | - |
| remainder | 余数 |   |
| assignment | 赋值 |   |
| indentation | 缩进 |   |
| scope | 变量可见性 |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
