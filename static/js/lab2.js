$(function(){//read
    //code

    $('.intput_item').focus(function(e){

        var this_obj = $(this);
        var  id = this_obj.attr("id");

        switch (id){
            case 'username':
                this_obj.next().text("6——18位数字、字母、下划线，需以字母开头");
                this_obj.next().css('color','#9e9e9e')

                break;
            case 'password':
                // this_obj.next().text("可通过手机号找回密码")


                break;
            case 'tel':
                this_obj.next().css('color','#9e9e9e')
                this_obj.next().text("可通过手机号找回密码")
                
                break;
            
            default:
                break; 
            }



    });

    $('.input_item').blur(function(e){

        var this_obj = $(this);

        var input_value = this_obj.val();
        var id = this_obj.attr("id");

        this_obj.next().text("");

        switch(id){
            case 'username':
                if(!isUsername(input_value)){

                    this_obj.next().text("请按要求输入邮箱地址");
                    this_obj.next().css('color','red')

                }

                
                break;

            case 'password':
                break;          
            case 'tel':
                if(!isTel(input_value)){

                    this_obj.next().text("请按要求输入手机号");
                    this_obj.next().css('color','red')

                }

                break;
            
            default:
                break;  
        }
    });
    
    $('#reg_btn').click(function(e){

        var username = $('#username').val()
        var tel = $('#tel').val()

        if(isUsername(username) && isTel(tel)){
            $('#username').submit();
        }



    });

    $('#psd_icon').click(function(e){

        var type = $('#password').attr('type');
        if (type == 'password'){

            $(this).css('background-image','url(../img/眼睛.png)')


            $('#password').attr('type','text')
        }else{
            $(this).css('background-image','url(../img/闭眼.png)')
            $('#password').attr('type','password')
            
        }

    });



    
});

















































































































