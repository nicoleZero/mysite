//获取项目列表
var ProjectInit = function(_cmbProject){
    var cmbProject = document.getElementById(_cmbProject);
    var options = "";
    //创建下拉选项
    function cmbAddOption(cmb,project_obj){
        console.log(project_obj);
        var option = document.createElement("option");
        cmb.options.add(option);
        option.innerHTML = project_obj.name;
        option.value = project_obj.id;
        //option.obj = obj;
    }
    function getProjectListInfo(){
        //获取某个用户列表的信息
        $.get("/project/get_project_list/",{},function(resp){
            if(resp.success==="true"){
                console.log(resp.data);
                let dataList = resp.data
                for(let i=0;i<dataList.length;i++){
                    cmbAddOption(cmbProject,dataList[i],dataList[i]);
                }
                //cmbSelect(cmbProject,defaultProject);

            }
            else{
                window.alert("请求失败");
            }
        });
    }
    getProjectListInfo();
};

