# NodeJS 与开发

## 1. Express 基础

### 1.1. npm 包模版

```json
{
  "name": "fcc-learn-npm-package-json", 
  "author": "hacker", 
  "description": "demo", 
  "keywords": [ "freecodecamp", "related", "words" ], 
  "license": "MIT", 
  "version": "1.2.0", 
  "dependencies": {
    // `^` 对 4.14.x 升级
    "express": "^4.14.0", 
    // `~` 对 2.x.x 升级
    "moment": "~2.14.0"
  }, 
  "main": "server.js", 
  "scripts": {
    "start": "node server.js"
  }, 
  "engines": {
    "node": "8.11.2"
  }, 
  "repository": {
    "type": "git", 
    "url": "https://idontknow/todo.git"
  }
}
```

### 1.2. 发送、获取

```javascript
var express = require("express");
var app = express();
// 控制台显示
console.log("hello world");
// 服务器发送
app.get("/", (req, res) => {
  res.send("Hello Express");
});
// 服务器发送文件
app.get("/", function(req, res) {
  res.sendFile(__dirname + "/views/index.html");
});
// 服务器发送 json
app.get("/json", (req, res) => {
  res.json({
    message: "Hello json"
  });
});
module.exports = app;

// 修改.env 文件
// .env MESSAGE_STYLE=uppercase
const message = "Hello json";
app.get("/json", (req, res) => {
  res.json(
        {"message": process.env.MESSAGE_STYLE === "uppercase" ? message.toUpperCase() : message
    })
});

// 服务器管理 assets 文件
app.use(express.static(__dirname + "/public"));
// Assets at the /assets route
app.use("/assets", express.static(__dirname + "/public"));

// 解析 POST
var bodyParser = require("body-parser");

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// 获取 POST 数据
app.post("/name", function(req, res) {
  // Handle the data in the request
  var string = req.body.first + " " + req.body.last;
  res.json({ name: string });
});
```

### 1.3. 中间件

```javascript
// 中间件
app.use(function middleware(req, res, next) {
  var string = req.method + " " + req.path + " - " + req.ip;
  next();
});

// 根目录中间件
var router = express.Router()

router.use(function middleware(req, res, next) {
  var string = req.method + " " + req.path + " - " + req.ip;
  console.log(string);
  next();
});

app.use('/', router)

// 串联中间件
app.get(
  "/now", 
  (req, res, next) => {
    req.time = new Date().toString();
    next();
  }, 
  (req, res) => {
    res.send({
      time: req.time
    });
  }
);

// 获取客户的路由参数
app.get("/:word/echo", (req, res) => {
  const { word } = req.params;
  res.json({
    echo: word
  });
});

// 获取客户的查询参数
app.get("/name", function(req, res) {
  var firstName = req.query.first;
  var lastName = req.query.last;
  var { first: firstName, last: lastName } = req.query;
  res.json({
    name: `${firstName} ${lastName}` 
  });
});
```

## 2. Mongoose

### 2.1. 创建

```javascript
// .env 
// GLITCH_DEBUGGER=true 
// SECRET=
// MADE_WITH=
// MONGO_URI=mongodb+srv://UcmsuLkvZHuZ3J:UcmsuLkvZHuZ3J@cluster0.gioh9.mongodb.net/<dbname>?retryWrites=true&w=majority
var express = require("express");
var app = express();

const mongoose = require("mongoose");
//mongoose.connect(process.env.MONGO_URI);
mongoose.connect(
  "mongodb+srv://UcmsuLkvZHuZ3J:UcmsuLkvZHuZ3J@cluster0.gioh9.mongodb.net/<dbname>?retryWrites=true&w=majority", 
  { useNewUrlParser: true, useUnifiedTopology: true }
);
console.log(process.env.MONGO_URI);

module.exports = app;

// 创建模型
const Schema = mongoose.Schema;
const personSchema = new Schema({
  name: { type: String, required: true }, 
  age: Number, 
  favoriteFoods: [String]
});

var Person = mongoose.model("Person", personSchema);

// 创建、存储
const createAndSavePerson = function(done) {
  let roughdoor = new Person({name: 'roughdoor', age: 2, favoriteFoods: ['meat', 'meat again']});
  roughdoor.save((err, data) => {
    if (err) return done(err);
    return done(null, data);
  })
};

// 创建多个
var arrayOfPeople = [
  {name: "Irina", age: 27, favoriteFoods: ["pane"]}, 
  {name: "marius", age: 26, favoriteFoods: ["pasta"]}, 
  {name: "catalina", age: 43, favoriteFoods: ["sarmale"]}
];

var createManyPeople = function(arrayOfPeople, done) {
  Person.create(arrayOfPeople, function (err, people) {
    if (err) return console.log(err);
    done(null, people);
  });
};
```

### 2.2. 查找

```javascript
// model.find()
var findPeopleByName = function(personName, done) {
  
  Person.find({name: personName}, (error, arrayOfResults) => {
    if(error){
      console.log(error)
    }else{
      done(null, arrayOfResults) 
    }
  })
};

// model.findOne()
var findOneByFood = function(food, done) {
  Person.findOne({favoriteFoods : {$all : [food]}}, (error, result) => {
    if(error){
      console.log(error)
    }else{
      done(null, result)
    }
  })
}

// model.findById()
var findEditThenSave = function(personId, done) {
  var foodToAdd = "hamburger";
  Person.findById(personId, (err, person) => {
    if(err) return console.log(err); 
  
    person.favoriteFoods.push(foodToAdd);

    person.save((err, updatedPerson) => {
      if(err) return console.log(err);
      done(null, updatedPerson)
    })
  })
};

// model.find()，串联（精确）查找
var queryChain = function(done) {
  var foodToSearch = "burrito";
  
  Person.find({favoriteFoods : foodToSearch})
    .sort({name: 'asc'})
    .limit(2)
    .select("-age") 
    .exec((error, filteredResults) => {
    if(error){
      console.log(error)
    }else{
      done(null, filteredResults)
    }
  })
};
```

### 2.3. 升级、删除

```javascript
// model.findOneAndUpdate()
const findAndUpdate = (personName, done) => {
  const ageToSet = 20;

  Person.findOneAndUpdate({name: personName}, {age: ageToSet}, {new: true}, (err, updatedDoc) => {
    if(err) return console.log(err);
    done(null, updatedDoc);
  })
};

// model.findByIdAndRemove()
var removeById = function(personId, done) {
  
  Person.findByIdAndRemove(personId, (error, deletedRecord) => {
    if(error){
      console.log(error)
    }else{
      done(null, deletedRecord)
    }
  })
};

// model.remove()，删除多个
const removeManyPeople = (done) => {
  const nameToRemove = "Mary";
  Person.remove({name: nameToRemove}, (err, response) => {
    if(err) return console.log(err);
    done(null, response);
  })
};
```

## 3. Express 进阶

### 3.1. connection

```javascript
require('dotenv').config();
const { MongoClient } = require('mongodb');

async function main(callback) {
    const URI = process.env.MONGO_URI; // Declare MONGO_URI in your .env file
    const client = new MongoClient(URI, { useNewUrlParser: true, useUnifiedTopology: true });

    try {
        // Connect to the MongoDB cluster
        await client.connect();

        // Make the appropriate DB calls
        await callback(client);

    } catch (e) {
        // Catch any errors
        console.error(e);
        throw new Error('Unable to Connect to Database')
    }
}

module.exports = main;
```

### 3.2. 引擎

```javascript
// server
"use strict";
require("dotenv").config();
const express = require("express");
const myDB = require("./connection");

const app = express();

app.use("/public", express.static(process.cwd() + "/public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.set("view engine", "pug");

app.route("/").get((req, res) => {
  res.render("pug/index.pug");
});

app.listen(process.env.PORT || 3000, () => {
  console.log("Listening on port " + process.env.PORT);
});
```

### 3.3. profile.pug

```javascript
html
  head
    title FCC Advanced Node and Express
    meta(name='description', content='Profile')
    meta(charset='utf-8')
    meta(http-equiv='X-UA-Compatible', content='IE=edge')
    meta(name='viewport', content='width=device-width, initial-scale=1')
    link(rel='stylesheet', href='/public/style.css')
  body
    h1.border.center FCC Advanced Node and Express Profile
    h2.center#welcome Welcome, #{username}!
    a(href='/logout') Logout
```

### 3.4. client.js

```javascript
// This file's full path is /public/client.js
const io = require("socket.io");
$(document).ready(function () {
  /* Global io */
  let socket = io();

  socket.on('user', (data) => {
    $('#num-users').text(data.currentUsers + ' users online');
    let message = data.name + (data.connected ? ' has joined the chat.' : ' has left the chat.');
    $('#messages').append($('<li>').html('<b>' + message + '</b>'));
  });

  socket.on('chat message', (data) => {
    console.log('socket.on 1');
    $('#messages').append($('<li>').text( `${data.name}: ${data.message}` ));
  });

  // Form submittion with new message in field with id 'm'
  $('form').submit(function () {
    let messageToSend = $('#m').val();
    // Send message to server here?
    socket.emit('chat message', messageToSend);
    $('#m').val('');
    return false; // Prevent form submit from refreshing page
  });
});
```

### 3.5. server.js

```javascript
'use strict';
require('dotenv').config();
const express = require('express');
const myDB = require('./connection');
const session = require('express-session');
const passport = require('passport');
const routes = require('./routes');
const auth = require('./auth.js');

const app = express();
const http = require('http').createServer(app);
const io = require('socket.io')(http);
const passportSocketIo = require('passport.socketio');
const cookieParser = require('cookie-parser');
const MongoStore = require('connect-mongo')(session);
const URI = process.env.MONGO_URI;
const store = new MongoStore({ url: URI });

app.set('view engine', 'pug');

app.use('/public', express.static(process.cwd() + '/public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.use(
  session({
    secret: process.env.SESSION_SECRET, 
    resave: true, 
    saveUninitialized: true, 
    cookie: { secure: false }, 
    key: "express.sid", 
    store: store
  })
);

app.use(passport.initialize());
app.use(passport.session());

io.use(
  passportSocketIo.authorize({
    cookieParser: cookieParser, 
    key: "express.sid", 
    secret: process.env.SESSION_SECRET, 
    store: store, 
    success: onAuthorizeSuccess, 
    fail: onAuthorizeFail
  })
);

myDB(async (client) => {
  const myDataBase = await client.db('database').collection('users');

  routes(app, myDataBase);
  auth(app, myDataBase);

  let currentUsers = 0;
  io.on('connection', (socket) => {
    ++currentUsers;
    io.emit('user', {
      name: socket.request.user.name, 
      currentUsers, 
      connected: true
    });
    socket.on('chat message', (message) => {
      io.emit('chat message', { name: socket.request.user.name, message });
    });
    console.log('A user has connected');
    socket.on('disconnect', () => {
      console.log('A user has disconnected');
      --currentUsers;
      io.emit('user', {
        name: socket.request.user.name, 
        currentUsers, 
        connected: false
      });
    });
  });
}).catch((e) => {
  app.route('/').get((req, res) => {
    res.render('pug', { title: e, message: 'Unable to login' });
  });
});

function onAuthorizeSuccess(data, accept) {
  console.log('successful connection to socket.io');

  accept(null, true);
}

function onAuthorizeFail(data, message, error, accept) {
  if (error) throw new Error(message);
  console.log('failed connection to socket.io:', message);
  accept(null, false);
}

http.listen(process.env.PORT || 3000, () => {
  console.log('Listening on port ' + process.env.PORT);
});
```

### 3.6. auth.js

```javascript
const passport = require("passport");
// 获取本地通行证
const LocalStrategy = require("passport-local");
const bcrypt = require("bcrypt");
// 获取用户 ID
const ObjectID = require("mongodb").ObjectID;
// GitHub 授权
const GitHubStrategy = require('passport-github').Strategy;

module.exports = function (app, myDataBase) {
  passport.serializeUser((user, done) => {
    done(null, user._id);
  });
  passport.deserializeUser((id, done) => {
    myDataBase.findOne({ _id: new ObjectID(id) }, (err, doc) => {
      if (err) return console.error(err);
      done(null, doc);
    });
  });
  passport.use(new LocalStrategy(
    function (username, password, done) {
      myDataBase.findOne({ username: username }, function (err, user) {
        console.log('User ' + username + ' attempted to log in.');
        if (err) { return done(err); }
        if (!user) { return done(null, false); }
        if (!bcrypt.compareSync(password, user.password)) { return done(null, false); }
        return done(null, user);
      });
    }
  ));

  passport.use(new GitHubStrategy({
      clientID: process.env.GITHUB_CLIENT_ID, 
      clientSecret: process.env.GITHUB_CLIENT_SECRET, 
      callbackURL: 'https://boilerplate-advancednode.your-username.repl.co/auth/github/callback'
    }, 
    function (accessToken, refreshToken, profile, cb) {
      console.log(profile);
      myDataBase.findAndModify(
        { id: profile.id }, 
        {}, 
        {
          $setOnInsert: {
            id: profile.id, 
            name: profile.displayName || 'John Doe', 
            photo: profile.photos[0].value || '', 
            email: Array.isArray(profile.emails) ? profile.emails[0].value : 'No public email', 
            created_on: new Date(), 
            provider: profile.provider || ''
          }, 
          $set: {
            last_login: new Date()
          }, 
          $inc: {
            login_count: 1
          }
        }, 
        { upsert: true, new: true }, 
        (err, doc) => {
          return cb(null, doc.value);
        }
      );
    }
  ));
};
```

### 3.7. routes.js

```javascript
const passport = require("passport");
// 加密
const bcrypt = require("bcrypt");

module.exports = function(app, myDataBase) {
  app.route("/").get((req, res) => {
    res.render("pug", {
      title: "Connected to Database", 
      message: "Please login", 
      showLogin: true, 
      showRegistration: true
    });
  });
  app
    .route("/login")
    .post(
      passport.authenticate("local", { failureRedirect: "/" }), 
      (req, res) => {
        res.redirect("/profile");
      }
    );
  app.route("/profile").get(ensureAuthenticated, (req, res) => {
    res.render("pug/profile", { username: req.user.username });
  });
  app.route("/logout").get((req, res) => {
    req.logout();
    res.redirect("/");
  });
  app.route("/register").post(
    (req, res, next) => {
      const hash = bcrypt.hashSync(req.body.password, 12);
      myDataBase.findOne({ username: req.body.username }, function(err, user) {
        if (err) {
          next(err);
        } else if (user) {
          res.redirect("/");
        } else {
          myDataBase.insertOne(
            { username: req.body.username, password: hash }, 
            (err, doc) => {
              if (err) {
                res.redirect("/");
              } else {
                next(null, doc.ops[0]);
              }
            }
          );
        }
      });
    }, 
    passport.authenticate("local", { failureRedirect: "/" }), 
    (req, res, next) => {
      res.redirect("/profile");
    }
  );

  app.route('/auth/github').get(passport.authenticate('github'));
  app.route('/auth/github/callback').get(passport.authenticate('github', { failureRedirect: '/' }), (req, res) => {
    res.redirect('/profile');
  });

  app.use((req, res, next) => {
    res
      .status(404)
      .type("text")
      .send("Not Found");
  });
};

// 中间件
function ensureAuthenticated(req, res, next) {
  if (req.isAuthenticated()) {
    return next();
  }
  res.redirect("/");
}
```

## 4. 单元测试

### 4.1. assertion-analyser

```javascript
function objParser(str, init) {
  // finds objects, arrays, strings, and function arguments
  // between parens, because they may contain ', '
  const openSym = ["[", "{", '"', "'", "("];
  const closeSym = ["]", "}", '"', "'", ")"];
  let type;
  for (var i = init || 0; i < str.length; i++) {
    type = openSym.indexOf(str[i]);
    if (type !== -1) break;
  }
  if (type === -1) return null;
  const open = openSym[type];
  const close = closeSym[type];
  let count = 1;
  for (var k = i + 1; k < str.length; k++) {
    if (open === '"' || open === "'") {
      if (str[k] === close) count--;
      if (str[k] === "\\") k++;
    } else {
      if (str[k] === open) count++;
      if (str[k] === close) count--;
    }
    if (count === 0) break;
  }
  if (count !== 0) return null;
  const obj = str.slice(i, k + 1);
  return {
    start: i, 
    end: k, 
    obj: obj, 
  };
}

function replacer(str) {
  // replace objects with a symbol ( __#n)
  let obj;
  let cnt = 0;
  let data = [];
  // obj = objParser(str) is not a syntax error
  while ((obj = objParser(str))) {
    data[cnt] = obj.obj;
    str =
      str.substring(0, obj.start) + "__#" + cnt++ + str.substring(obj.end + 1);
  }
  return {
    str: str, 
    dictionary: data, 
  };
}

function splitter(str) {
  // split on commas, then restore the objects
  const strObj = replacer(str);
  let args = strObj.str.split(", ");
  args = args.map(function (a) {
    let m = a.match(/__#(\d+)/);
    while (m) {
      a = a.replace(/__#(\d+)/, strObj.dictionary[m[1]]);
      m = a.match(/__#(\d+)/);
    }
    return a.trim();
  });
  return args;
}

function assertionAnalyser(body) {
  // already filtered in the test runner
  // // remove comments
  // body = body.replace(/\/\/.*\n|\/\*.*\*\//g, '');
  // // get test function body
  // body = body.match(/\{\s*([\s\S]*)\}\s*$/)[1];

  if (!body) return "invalid assertion";
  // replace assertions bodies, so that they cannot
  // contain the word 'assertion'

  const cleanedBody = body.match(
    /(?:browser\s*\.\s*)?assert\s*\.\s*\w*\([\s\S]*\)/
  );
  if (cleanedBody && Array.isArray(cleanedBody)) {
    body = cleanedBody[0];
  } else {
    // No assertions present
    return [];
  }
  const s = replacer(body);
  // split on 'assertion'
  const splittedAssertions = s.str.split("assert");
  let assertions = splittedAssertions.slice(1);
  // match the METHODS

  let assertionBodies = [];
  const methods = assertions.map(function (a, i) {
    const m = a.match(/^\s*\.\s*(\w+)__#(\d+)/);
    assertionBodies.push(parseInt(m[2]));
    const pre = splittedAssertions[i].match(/browser\s*\.\s*/)
      ? "browser."
      : "";
    return pre + m[1];
  });
  if (
    methods.some(function (m) {
      return !m;
    })
  )
    return "invalid assertion";
  // remove parens from the assertions bodies
  const bodies = assertionBodies.map(function (b) {
    return s.dictionary[b].slice(1, -1).trim();
  });
  assertions = methods.map(function (m, i) {
    return {
      method: m, 
      args: splitter(bodies[i]), //replace objects, split on ', ' , then restore objects
    };
  });
  return assertions;
}

module.exports = assertionAnalyser;
```

### 4.2. test-runner

```javascript
const analyser = require("./assertion-analyser");
const EventEmitter = require("events").EventEmitter;

const Mocha = require("mocha"), 
  fs = require("fs"), 
  path = require("path");

const mocha = new Mocha();
const testDir = "./tests";

// Add each .js file to the mocha instance
fs.readdirSync(testDir)
  .filter(function(file) {
    // Only keep the .js files
    return file.substr(-3) === ".js";
  })
  .forEach(function(file) {
    mocha.addFile(path.join(testDir, file));
  });

const emitter = new EventEmitter();
emitter.run = function() {
  const tests = [];
  let context = "";
  const separator = " -> ";
  // Run the tests.
  try {
    const runner = mocha
      .ui("tdd")
      .run()
      .on("test end", function(test) {
        // remove comments
        let body = test.body.replace(/\/\/.*\n|\/\*.*\*\//g, "");
        // collapse spaces
        body = body.replace(/\s+/g, " ");
        const obj = {
          title: test.title, 
          context: context.slice(0, -separator.length), 
          state: test.state, 
          // body: body, 
          assertions: analyser(body)
        };
        tests.push(obj);
      })
      .on("end", function() {
        emitter.report = tests;
        emitter.emit("done", tests);
      })
      .on("suite", function(s) {
        context += s.title + separator;
      })
      .on("suite end", function(s) {
        context = context.slice(0, -(s.title.length + separator.length));
      });
  } catch (e) {
    throw e;
  }
};

module.exports = emitter;
```

### 4.3. 基础测试

```javascript
const chai = require("chai");
const assert = chai.assert;

suite("Basic Assertions", function () {
  /** Use assert.isNull() or assert.isNotNull() to make the tests pass. **/
  test("#isNull, #isNotNull", function () {
    assert.isNull(
      null, 
      "this is an optional error description - e.g. null is null"
    );
    assert.isNotNull(1, "1 is not null");
  });
  /** Use assert.isDefined() or assert.isUndefined() to make the tests pass. **/
  test("#isDefined, #isUndefined", function () {
    assert.isDefined(null, "null is not undefined");
    assert.isUndefined(undefined, "undefined IS undefined");
    assert.isDefined("hello", "a string is not undefined");
  });
  /** Use assert.isOk() or assert.isNotOk() to make the tests pass. **/
  // .isOk(truthy) and .isNotOk(falsey) will pass
  test("#isOk, #isNotOk", function () {
    assert.isNotOk(null, "null is falsey");
    assert.isOk("I'm truthy", "a string is truthy");
    assert.isOk(true, "true is truthy");
  });
  /** Use assert.isTrue() or assert.isNotTrue() to make the tests pass. **/
  // .isTrue(true) and .isNotTrue(everything else) will pass.
  // .isFalse() and .isNotFalse() also exist.
  test("#isTrue, #isNotTrue", function () {
    assert.isTrue(true, "true is true");
    assert.isTrue(!!"double negation", "double negation of a truthy is true");
    assert.isNotTrue(
      { value: "truthy" }, 
      "A truthy object is NOT TRUE (neither is false...)"
    );
  });
});
```

### 4.4. 相等

```javascript
suite("Equality", function () {
  /** .equal(), .notEqual() **/
  // .equal() compares objects using '=='
  test("#equal, #notEqual", function () {
    assert.equal(12, "12", "numbers are coerced into strings with == ");
    assert.notEqual(
      { value: 1 }, 
      { value: 1 }, 
      "== compares object references"
    );
    assert.equal(6 * "2", "12", "no more hints...");
    assert.notEqual(6 + "2", "12", "type your error message if you want");
  });
  /** .strictEqual(), .notStrictEqual() **/
  // .strictEqual() compares objects using '==='
  test("#strictEqual, #notStrictEqual", function () {
    assert.notStrictEqual(6, "6");
    assert.strictEqual(6, 3 * 2);
    assert.strictEqual(6 * "2", 12);
    assert.notStrictEqual([1, "a", {}], [1, "a", {}]);
  });
  /** .deepEqual(), .notDeepEqual() **/
  // .deepEqual() asserts that two object are deep equal
  test("#deepEqual, #notDeepEqual", function () {
    assert.deepEqual(
      { a: "1", b: 5 }, 
      { b: 5, a: "1" }, 
      "keys order doesn't matter"
    );
    assert.notDeepEqual(
      { a: [5, 6] }, 
      { a: [6, 5] }, 
      "array elements position does matter !!"
    );
  });
});
```

### 4.5. 比较

```javascript
suite("Comparisons", function () {
  /** .isAbove() => a > b , .isAtMost() => a <= b **/
  test("#isAbove, #isAtMost", function () {
    assert.isAtMost("hello".length, 5);
    assert.isAbove(1, 0);
    assert.isAbove(Math.PI, 3);
    assert.isAtMost(1 - Math.random(), 1);
  });
  /** .isBelow() => a < b , .isAtLeast =>  a >= b **/
  test("#isBelow, #isAtLeast", function () {
    assert.isAtLeast("world".length, 5);
    assert.isAtLeast(2 * Math.random(), 0);
    assert.isBelow(5 % 2, 2);
    assert.isBelow(2 / 3, 1);
  });
  /** .approximately **/
  // .approximately(actual, expected, range, [message])
  // actual = expected +/- range
  // Choose the minimum range (3rd parameter) to make the test always pass
  // it should be less than 1
  test("#approximately", function () {
    assert.approximately(weirdNumbers(0.5), 1, /*edit this*/ 0.5);
    assert.approximately(weirdNumbers(0.2), 1, /*edit this*/ 0.8);
  });
});
```

### 4.6. 数组

```javascript
suite("Arrays", function () {
  /** #isArray vs #isNotArray **/
  test("#isArray, #isNotArray", function () {
    assert.isArray(
      "isThisAnArray?".split(""), 
      "String.prototype.split() returns an Array"
    );
    assert.isNotArray([1, 2, 3].indexOf(2), "indexOf returns a number.");
  });
  /** #include vs #notInclude **/
  test("Array #include, #notInclude", function () {
    assert.notInclude(winterMonths, "jul", "It's summer in july...");
    assert.include(
      backendLanguages, 
      "javascript", 
      "JS is a backend language !!"
    );
  });
});
```

### 4.7. 字符串

```javascript
suite("Strings", function () {
  /** #isString asserts that the actual value is a string. **/
  test("#isString, #isNotString", function () {
    assert.isNotString(Math.sin(Math.PI / 4), "a float is not a string");
    assert.isString(process.env.PATH, "env vars are strings (or undefined)");
    assert.isString(JSON.stringify({ type: "object" }), "a JSON is a string");
  });
  /** #include (on #notInclude ) works for strings too !! **/
  // It asserts that the actual string contains the expected substring
  test("String #include, #notInclude", function () {
    assert.include("Arrow", "row", "Arrow contains row...");
    assert.notInclude("dart", "queue", "But a dart doesn't contain a queue");
  });
  /** #match Asserts that th actual value **/
  // matches the second argument regular expression.
  test("#match, #notMatch", function () {
    var regex = /^#\sname\:\s[\w\s]+, \sage\:\s\d+\s?$/;
    assert.match(formatPeople("John Doe", 35), regex);
    assert.notMatch(formatPeople("Paul Smith III", "twenty-four"), regex);
  });
});
```

### 4.8. 对象

```javascript
/** #property asserts that the actual object has a given property. **/
// Use #property or #notProperty where appropriate
suite("Objects", function () {
  test("#property, #notProperty", function () {
    assert.notProperty(myCar, "wings", "A car has not wings");
    assert.property(airlinePlane, "engines", "planes have engines");
    assert.property(myCar, "wheels", "Cars have wheels");
  });
  /** #typeOf asserts that value’s type is the given string, **/
  // as determined by Object.prototype.toString.
  // Use #typeOf or #notTypeOf where appropriate
  test("#typeof, #notTypeOf", function () {
    assert.typeOf(myCar, "object");
    assert.typeOf(myCar.model, "string");
    assert.notTypeOf(airlinePlane.wings, "string");
    assert.typeOf(airlinePlane.engines, "array");
    assert.typeOf(myCar.wheels, "number");
  });
  /** #instanceOf asserts that an object is an instance of a constructor **/
  // Use #instanceOf or #notInstanceOf where appropriate
  test("#instanceOf, #notInstanceOf", function () {
    assert.notInstanceOf(myCar, Plane);
    assert.instanceOf(airlinePlane, Plane);
    assert.instanceOf(airlinePlane, Object, "everything is an Object");
    assert.notInstanceOf(myCar.wheels, String);
  });
});
```

## 5. 功能测试

### 5.1. 断点、响应

```javascript
const chai = require("chai");
const assert = chai.assert;

const server = require("../server");
const chaiHttp = require("chai-http");
chai.use(chaiHttp);

suite("Integration tests with chai-http", function () {
  test("Test GET /hello with no name", function (done) {
    chai
      .request(server) // 'server' is the Express App
      .get("/hello") // http_method(url). NO NAME in the query !
      .end(function (err, res) {
        assert.equal(res.status, 200);
        assert.equal(res.text, "hello Guest");
        done();
      });
  });

  test("Test GET /hello with your name", function (done) {
    chai
      .request(server) // 'server' is the Express App
      .get("/hello?name=John") /** <=== Put your name in the query **/
      .end(function (err, res) {
        assert.equal(res.status, 200);
        assert.equal(res.text, "hello John");
        done(); 
      });
  });
  
  test('send {surname: "Colombo"}', function (done) {
    chai
      .request(server)
      .put("/travellers")
      .send({ surname: "Colombo" })
      .end(function (err, res) {
        assert.equal(res.status, 200, "response status should be 200");
        assert.equal(res.type, "application/json", "Response should be json");
        assert.equal(
          res.body.name, 
          "Cristoforo", 
          'res.body.name should be "Christoforo"'
        );
        assert.equal(
          res.body.surname, 
          "Colombo", 
          'res.body.surname should be "Colombo"'
        );
        done();
      });
  });

  test('send {surname: "da Verrazzano"}', function (done) {
    chai
      .request(server)
      .put("/travellers")
      .send({ surname: "da Verrazzano" })
      .end(function (err, res) {
        assert.equal(res.status, 200, "response status should be 200");
        assert.equal(res.type, "application/json", "Response should be json");
        assert.equal(res.body.name, "Giovanni");
        assert.equal(res.body.surname, "da Verrazzano");

        done();
      });
  });
});
```

### 5.2. 无头浏览器

```javascript
const Browser = require("zombie");

suite('"Famous Italian Explorers" form', function () {
  test('submit "surname" : "Colombo" - write your e2e test...', function (done) {
    browser.fill("surname", "Colombo").pressButton("submit", function () {
      browser.assert.success();
      browser.assert.text("span#name", "Cristoforo");
      browser.assert.text("span#surname", "Colombo");
      browser.assert.element("span#dates", 1);
      done();
    });
  });
});
```
