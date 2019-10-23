$(".bsj-pact>li").click(function() {       /*----------------选项卡的点击事件，移动端用tap-----------------*/
                    $(this).css({/*选中选项卡的样式*/
                        color: "#ff4200",
                        borderBottom: "1px solid #ff4200"

                    }).siblings().css({/*未选中选项卡的样式*/
                        color: "#000000",
                        borderBottom: "none"
                    });
                });

                $(".bsj-pact li").click(function() { /*----------------选项卡的点击事件，移动端用tap-----------------*/
                    $(this).addClass("action").siblings().removeClass("action");/*选中的li添加action类，其他的移除*/
                    var index = $(this).index();/*定义索引数值*/
                    $(".pact-content li").eq(index).css("display", "block").siblings().css("display", "none");/*相对应的第几个内容区显示，其他的隐藏*/
                });