function isUsername(username){
    var reg = /^[a-zA-Z]\w{5,17}$/;

    return reg.test(username);
    

}
function isPassword(password){
    // 8-16位，必须包含字母和数字
    var reg = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,16}$/;
    return reg.test(password);
}

function isTel(tel){
    var reg = /^1[3-9]\d{9}$/;
    return reg.test(tel);
}
