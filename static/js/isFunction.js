function isUsername(username){
    var reg = /^[a-zA-Z]\w{5,17}$/;

    return reg.test(username);
    

}
function isTel(tel){
    var reg = /^1[3-9]\d{9}$/;
    return reg.test(tel);
}
