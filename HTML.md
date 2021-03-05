## 三大语言

- HTML：定义网页结构

- CSS：定义网页样式 

- JavaScript：定义网页中与用户交互的部分



## HTML5

超文本标记语言，用于定义网页的结构。通常有开始和结束标签，例如`<p> </p>`， 不区分大小写。



### HTML Structure

HTML里的各类结构，代码结构，文件结构，结构标签等。

#### 1. HTML 代码结构<img src="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics/grumpy-cat-small.png">

<img src="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics/grumpy-cat-attribute-small.png">

- class称为*attribute name*, editor-note称为*attribute value*.

- 一个Attribute需要有空格跟之前的元素隔开，后跟一个`=`号，*attibute value*需要用双引号括起来。



#### 2. HTML文件结构

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <!-- 向用户展示的内容 -->
  </body>
</html>
```



#### 3. 结构标签

- `head`    网页信息，**非向用户展示的内容**
  - meta elements:  `link`, `meta`, `title`, and `style`, etc
  
- `main`  页面主要内容

- `body`    网页内容，**向用户展示的内容**
   - `h1`-`h6`  
   -  `p`  
- `header`   用在`body`里
  - `h1`
   - `nav`

- `footer`  页脚

- `article`   独立的，分离的内容

- `section `   各自相关的内容

- `div`  分割元素

> If a book is the ` article`, then each chapter is a `section` When there's no relationship between groups of content, then use a `div`.



### 媒体

#### 1. 图片

- `img`  图片标签
- `src`  图片链接
- `alt`  说明，在图片无法加载时显示
- `width`  `height`  更改图片宽、高

```html
<img src="https://www.freecatphotoapp.com/your-image.jpg" alt="A business cat wearing a necktie." width="100" height="60">

<!--将图片变链接，`href` 后的链接需要跟图片链接是一个主域名，不然无法跳转 -->
  <a href="https://catchypianos.com"><img src="https://catchypianos.com/wp-content/uploads/2020/10/yamaha-p45-digital-piano-768x433.jpg" alt="A Piano."></a>
```

#### 2. 音频

- `audio`  音频标签
- `controls`  音频控制条
- `scr`  音频资源链接

```HTML
<audio controls>
  <source src="https://s3.amazonaws.com/freecodecamp/screen-reader.mp3" type="audio/mpeg" />
</audio>
```



### 锚文本

#### 1. 锚文本链接

```html
<a href="https://freecodecamp.org">this links to freecodecamp.org</a>
```

> `src` 外部链接，`href` 内部链接，没有链接则用 `href="#"`



#### 2. 锚文本跳转

```html
<a href="#footer">Jump to Bottom</a>
...
<footer id="footer">Copyright Cat Photo App</footer>
```

> `href`和`id`后面一样，`href`后面的要加`#`

> 匹配的是id，不是锚文本



### 输入框

`input`   字输入框，单选框，多选框，日期选框等

- `form`  上传数据
- `fieldset`  段落框，选项外面会有一个框
  - `legend`  段落框标题
- `label`  单选框多选框中点击文本也可选中
- `button`  按钮上传内容

```html
<!-- 上传数据到`action` 后面的url -->
<form action="https://freecatphotoapp.com/submit-cat-photo">
    <input type="text" placeholder="cat photo URL">
    <button type="submit">submit</button>
</form>
```
<hr></hr>

| input里的attribute |                                                |
| ------------------ | ---------------------------------------------- |
| `type`             | 常见`text`, `submit`, `date`，见下表           |
| `placeholder`      | 字框中未输入时显示的文字                       |
| `id`               | 为了和`label`里的`for`对应                     |
| `name`             | 一组多选框或单选框用同一个`name`，显示是一个组 |
| `value`            | 选框中用于识别选项                             |

```html
<label for="loving">
<!--`value`是用于选框中创建了选项，需要创建`value`去识别用户所选，比如选择了indoor，会出现`indoor-outdoor=indoor`，如果不加value，会出现`indoor-outdoor=on`，不利于识别。 -->
<input id="loving" value="loving" type="checkbox" name="personality"> Loving</label>
```
<hr></hr>

| Type 类型  |        |
| ---------- | ------ |
| `text`     | 文字   |
| `submit`   | 按钮   |
| `radio`    | 单选框 |
| `checkbox` | 多选框 |
| `date`     | 日期   |



#### 1. 字框

`type="text"`

- `placeholder`  未输入时显示的文字


- `required`  把输入框变成必填

```html
<input type="text" placeholder="cat photo URL" required>
```



#### 2. 单选框

`tyle="radio"`

```html
<form>
  <fieldset>
    <legend>Choose one of these three items:</legend>
    <label> 
<!--所有选项需要采用一个`name`去形成一个组 -->
    <input type="radio" name="indoor-outdoor">Indoor 
    </label>
    <label> 
    <input type="radio" name="indoor-outdoor">Outdoor
    </label>
<!-- for和id是为了对应点击的按钮，一个`label`可能会出现多个`input` -->
    <label for="outdoor"> 
    <input type="radio" name="indoor-outdoor">Indoor
    <input id="outdoor" type="radio" name="indoor-outdoor">Outdoor
    </label>
    </fieldset>
</form>
```



#### 3. 多选框

`tyle="checkbox"`

```html
<label for="loving"><input id="loving" type="checkbox" name="personality"> Loving</label>
```



#### 4. 日期框

`type="date"`

```html
<label for="pickdate">Enter a date:</label>
<input type="date" id="pickdate" name="date">
```



### 列表

```HTML
<html>
    <p>Things cats love:</p>
<!-- unordered list，出来的样子是有bullet point -->
    <ul>
      <li>milk</li>
      <li>cheese</li>
    </ul>
<!-- ordered list，出来的样子是有数字序号 -->
    <ol>
      <li>Garfield</li>
      <li>Sylvester</li>
    </ol>
</html>
```



## FCC 第一章课


1. HTML: Structure + Semantics
2. CSS: Layout + Appearance
3. Visual Design: Presentation + User Experience  动态表现
4. Applied Accessibility: Keyboard-friendly; Text alternatives exist
5. CSS Flexbox: Arranges elements in a predictable way **for different screen sizes and browsers**; Create page layouts for a dynamic UI
6. CSS Grid: Place children elements where you want within the grid




