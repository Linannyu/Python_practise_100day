# CSS 笔记

---

# 一、margin

**定义：**

margin 是 CSS 中的外边距，用于控制元素与其他元素之间的距离。margin 属性可以接受四个值，分别表示上、右、下、左四个方向的外边距。

**例子：**

```css
margin: 10px 20px 30px 40px;
```

顺序是：

> 上 → 右 → 下 → 左

也可以单独设置哪一个位置：

```css
margin-top: 20px;      /* 上 */
margin-right: 10px;    /* 右 */
margin-bottom: 30px;   /* 下 */
margin-left: 15px;     /* 左 */
```

```css
margin: auto;
```

经常用于让块级元素水平居中。

---

# 二、padding

**定义：**

padding 是 CSS 中的内边距，表示内容（Content）与边框（Border）之间的距离。

**例子：**

```css
.box {
    padding: 20px;
}
```

```html
<div class="box">Hello</div>
```

效果是：

> 文字 Hello 不会紧贴边框，而是距离边框 20px。

四个位置都可以单独写，顺序同 margin。

---

# 三、overflow

**定义：**

CSS overflow 属性用于控制内容溢出元素框时显示的方式。

**值：**

| 值 | 描述 |
|------|------|
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。 |
| hidden | 内容会被修剪，并且其余内容是不可见的。 |
| scroll | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。 |

---

# 四、Float

**定义：**

CSS 的 Float（浮动），会使元素向左或向右移动，其周围的元素也会重新排列。

## 清除浮动 - 使用 clear

元素浮动之后，周围的元素会重新排列，为了避免这种情况，使用 clear 属性。

clear 属性指定元素两侧不能出现浮动元素。

**例子：**

```css
img {
    float: left;
    margin-right: 10px;
}

h2, p {
    clear: left;
}
```

---

# 五、list-style-type

**定义：**

去掉列表项前面的标记（圆点、数字等）。

| 值 | 描述 |
|------|------|
| none | 无标记。 |
| disc | 默认。标记是实心圆。 |
| circle | 标记是空心圆。 |
| square | 标记是实心方块。 |
| decimal | 标记是数字。 |
| decimal-leading-zero | 0开头的数字标记。(01, 02, 03, 等。) |
| lower-roman | 小写罗马数字(i, ii, iii, iv, v, 等。) |
| upper-roman | 大写罗马数字(I, II, III, IV, V, 等。) |
| lower-alpha | 小写英文字母 The marker is lower-alpha (a, b, c, d, e, 等。) |
| upper-alpha | 大写英文字母 The marker is upper-alpha (A, B, C, D, E, 等。) |
| lower-greek | 小写希腊字母(alpha, beta, gamma, 等。) |
| lower-latin | 小写拉丁字母(a, b, c, d, e, 等。) |
| upper-latin | 大写拉丁字母(A, B, C, D, E, 等。) |
| hebrew | 传统的希伯来编号方式。 |
| armenian | 传统的亚美尼亚编号方式。 |
| georgian | 传统的乔治亚编号方式(an, ban, gan, 等。) |
| cjk-ideographic | 简单的表意数字。 |
| hiragana | 标记是：a, i, u, e, o, ka, ki, 等。（日文平假名字符） |
| katakana | 标记是：A, I, U, E, O, KA, KI, 等。（日文片假名字符） |
| hiragana-iroha | 标记是：i, ro, ha, ni, ho, he, to, 等。（日文平假名序号） |
| katakana-iroha | 标记是：I, RO, HA, NI, HO, HE, TO, 等。（日文片假名序号） |

# 六.justify-content
**定义：**

CSS 属性用于设置弹性盒子元素在主轴（默认横轴）方向上的对齐方式。

**值：**

| 值 | 描述 |
|------|------|
| flex-start | 默认值。从行首起始位置开始排列。	 |
| flex-end | 从行尾位置开始排列。 |
| center | 居中排列。 |
| space-between | 均匀排列每个元素，首个元素放置于起点，末尾元素放置于终点。 |
| space-evenly	 | 均匀排列每个元素，每个元素之间的间隔相等。 |
| space-around | 均匀排列每个元素，每个元素周围分配相同的空间。	 |
| initial | 设置该属性为它的默认值。请参阅 initial。 |
| inherit | 从父元素继承该属性。请参阅 inherit。 |