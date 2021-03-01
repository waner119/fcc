# JavaScript

JS是一种脚本语言，用于页面交互，适配于所有现在的浏览器。



## 杂

- 注释

  - `//`  单行注释
  - `/*  */` 多行注释

  

## JS 八种数据类型

### undefined 未定义

### null 空值

### boolean  布尔值

### string  字符串

### symbol 符号

### BigInt  比2<sup>53</sup> -1 大的数值





### number  数值



### object

  

## 赋值

  `variable`

  命名可用数字，字母，`$`, `_` 命名，不可包含空格或用数字开头，命名区分大小写。建议的命名方式 `camelCase`，即第一个单词首字母小写，之后的单词首字母皆大写。

```js
var myVar;
myVar = 5;
```

**1. 储存多值**

Array   可以储存多个数据类型，用逗号隔开

```js
//单个方括号
var myArray = ["Katelyn", 25];
//多个方括号, 括号内外都要逗号隔开
var myArray = [["Katelyn", 25], ["Kate", 30]];
```



**1.1 多值内引**

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



**2. 多次使用的值**

`function`

```js
function reusableFunction() {
  console.log("Hi World");
}
reusableFunction();  //使用这个会运行{}里的所有代码
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

| 代码   | 意思         |      |
| ------ | ------------ | ---- |
| `i++;` | `i = i + 1;` |      |
| `i--;` | `i = i - 1;` |      |
|        |              |      |



**3. 运算符号**

| 符号 | 运算方式 | 例子         | 备注             |
| ---- | -------- | ------------ | ---------------- |
| %    | 余数     | `17 % 2` = 1 | 不适宜用在负数上 |
|      |          |              |                  |
|      |          |              |                  |

> 17 - 2\*2*2\*2 = 1



**4. 加减乘除复合赋值**

​       `+=`   `-=`   `*=`   `/=`

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

| 字符 | 意思          | 备注 |
| ---- | ------------- | ---- |
| `\'` | 单引号        |      |
| `\"` | 双引号        |      |
| `\n` | 新的一行      |      |
| `\r` | 回车          |      |
| `\t` | tab           |      |
| `\b` | word boundary |      |
| `\f` | form feed     |      |



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







## 专业词汇

| 单词        | 意思 | 备注 |
| ----------- | ---- | ---- |
| remainder   | 余数 |      |
| assignment  | 赋值 |      |
| indentation | 缩进 |      |
|             |      |      |
|             |      |      |
|             |      |      |
|             |      |      |
|             |      |      |
|             |      |      |

