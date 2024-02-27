var spisok = '';
var kilkist = 1;


function AddBlock()
{
    let n = document.getElementsByClassName('block');
    let data = new Array();
    let data2 = new Array();

    document.querySelectorAll('input').forEach(input =>data.push(input.value));
    document.querySelectorAll('textarea').forEach(input =>data2.push(input.value));
    data.pop();
    data.pop();
    data.pop();
    kilkist = document.getElementsByClassName('block').length +1;
    console.log(kilkist)
    var dummy = '<div class="block">Назва:<br><input type="text" name="name'+kilkist+'" id="name"><br>Текст:<br><textarea form="course" name="text'+kilkist+'" id="text" maxlength="250" rows="7" cols="95" style="resize: none;"></textarea><br>Файл:<br><div class="addimageopisanieblock"><img src="/static/img/file.png"></div><br><hr></div>';
    var buttons = '<div class="submitbuttonblock" id="submitbuttonblock">\n' +
        '                    <input type="button" value="Додати блок" class="submitbutton" id="newblock" onclick="AddBlock()">\n' +
        '                    <input type="button" value="Видалити блок" class="submitbutton" id="delblock" onclick="DeleteBlock()">\n' +
        '                    <input type="submit" value="Завантажити" class="submitbutton">\n' +
        '                </div>'
    document.getElementById("submitbuttonblock").remove();
    document.getElementById("allblocks").innerHTML += dummy;
    document.getElementById("allblocks").innerHTML += buttons;

    let inputs = document.querySelectorAll('input');
    let areas = document.querySelectorAll('textarea');
    inputs[0].value = data[0];
    for (let i = 0; i < kilkist-1; i++)
    {
        inputs[i+1].value = data[i+1];
        areas[i].value = data2[i];
    }
}
function DeleteBlock()
{
    let n = document.getElementsByClassName('block');
    kilkist--;
    console.log(kilkist)
    if(n.length == 2)
    {
        document.getElementById('delblock').disabled = true;
    }
    if(n.length != 1)
    {
        let del = n[n.length-1]
        del.parentNode.removeChild(del)
    }

}
function Del(kilkist2) {
    let n = document.getElementsByClassName('block');
    if(n.length == 1)
    {
        if(n[0].value == "Don't delete me i'm the last(" || n[0].value == ":P"){
            n[0].value = ":P";
        }
        else{
            n[0].value = "Don't delete me i'm the last(";
        }
    }
    else {
        document.getElementById("komp" + kilkist2).remove();
	    konkaten();
    }
}


function Add() {
	let n = document.getElementsByClassName('kompozpole');
	let arr = new Array();
    for(let i = 0; i < n.length; i++){
        arr[i] = n[i].value;
    }

    kilkist++;
    var dummy = '<div class="kompozblock" id="komp' + kilkist + '"> <input class="kompozpole" type="text" name="track" onkeyup="konkaten()"> <input class="delkompoz" type="button" value="X" onclick="Del(' + kilkist + ')"> </div>';
    document.getElementById("allkompoz").innerHTML += dummy;

	for(let i = 0; i < arr.length; i++){
		n[i].value = arr[i];
    }
}

function konkaten() {
	let n = document.getElementsByClassName('kompozpole');
	list = '';
	for(let i = 0; i < n.length; i++){
		if(n[i].value != ''){
			list += n[i].value + ';';
		}
    }

	if(list.length > 0){
		document.getElementById("track1").value = list.slice(0, -1);
	}
};

// Image

var loadFile = function(event) {
	var output = document.getElementById('imagefile');
	a = URL.createObjectURL(event.target.files[0]);
	output.style.backgroundImage = "url(" + a + ")";
	output.value = '';
	output.style.border = "1px solid black";
};


document.addEventListener("DOMContentLoaded", () => {
    konkaten();
  });


function getCookie(cname) {
  let name = cname + "=";
  let decodedCookie = decodeURIComponent(document.cookie);
  let ca = decodedCookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}

function AddToCart(id)
{
    let product = getCookie(id)

    if (product != "")
    {
        document.cookie = id + '=' + (1 + parseInt(product)) + ';path=/;'
    }
    else
    {
        document.cookie = id + '=' + 1 + ';path=/;'
    }
    console.log(document.cookie)
    document.getElementsByClassName('addedbasket')[0].style.display = "flex"
}

function UpdateCart(id)
{

    let elements = document.querySelectorAll('.count')
    let texts = document.querySelectorAll('.ID')
    let text = []
    for ( let txt of texts)
    {
        text.push(txt.innerHTML)
    }

    let counter = 0
    for (let el of elements)
    {
        if(text[counter] == id)
        {
            let tmp = el.innerHTML
            tmp = tmp.split(':')
            tmp[1] = parseInt(tmp[1]) + 1
            el.innerHTML = tmp[0] + ': ' + tmp[1]
        }
        counter ++
    }
}

function UpdateCartMinus(id)
{

    let elements = document.querySelectorAll('.count')
    let texts = document.querySelectorAll('.ID')
    let text = []
    for ( let txt of texts)
    {
        text.push(txt.innerHTML)
    }

    let counter = 0
    for (let el of elements)
    {
        if(text[counter] == id)
        {
            let tmp = el.innerHTML
            tmp = tmp.split(':')
            if(tmp[1] > 1)
                tmp[1] = parseInt(tmp[1]) - 1
            el.innerHTML = tmp[0] + ': ' + tmp[1]
        }
        counter ++
    }
}

function PlusToCart(id)
{
    let product = getCookie(id)

    if (product != "")
    {
        document.cookie = id + '=' + (1 + parseInt(product)) + ';path=/;'
    }
    else
    {
        document.cookie = id + '=' + 1 + ';path=/;'
    }
    UpdateCart(id)
    console.log(document.cookie)
    UpdateSum()
}

function RemoveFromCart(id)
{
    let product = getCookie(id)

    if (product != "")
    {
        if (parseInt(product) > 1)
        {
            document.cookie = id + '=' + (parseInt(product) - 1) + ';path=/;'
        }
    }
    else
    {
        document.cookie = id + '=' + 1 + ';path=/;'
    }
    UpdateCartMinus(id)
    console.log(document.cookie)
    UpdateSum()
}

function DeleteFromCart(id)
{
    let product = getCookie(id)
    if (product != "")
    {
        document.cookie = id + '=' + (parseInt(product) - 1) + ';path=/;expires=Thu, 01 Jan 1970 00:00:01 GMT'
    }
    document.location.reload(true)
    console.log(document.cookie)
    UpdateSum()
}

function UpdateSum()
{
    let count = document.querySelectorAll('.count')
    let price = document.querySelectorAll('.price')

    let sum = 0.0;
    for(let i = 0; i < price.length; i++)
    {
        sum += parseFloat(count[i].innerHTML.split(':')[1]) * parseFloat(price[i].innerHTML.split(' ')[2])
    }
    document.querySelector('.sum').innerHTML = "Сумма: " + sum.toFixed(1).toString()
}

function ClearCart()
{
    let cookies = document.cookie.split(";");
    console.log(cookies)

    for (let i = 0; i < cookies.length; i++)
    {
        let cookie = cookies[i];
        let eqPos = cookie.indexOf("=");
        let name = eqPos > -1 ? cookie.substr(0, eqPos) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/";
    }
}
