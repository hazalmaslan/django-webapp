var arr = [];

function remove(arr, value) {
    return arr.filter(function(ele) {
        return ele !== value;
    });
}

function addSizeVal() {
    var sizeVal = document.getElementById("size").value;
    var sizeType = "";
    var sizeMag = "";

    if (sizeVal !== "" || sizeType === "" || sizeMag === "") {
        sizeType = $('input[name=size-val]:checked').val();
        sizeMag = $('input[name=size-mag]:checked').val();
    }
    else{
        alert("Please select all the choices");
    }
    if(typeof sizeVal === 'number'){

    }
    var str = "size:" + sizeVal + " " + sizeType + " " + sizeMag;
    if (document.getElementById("plus-size-button").checked) {
        arr.push(str);
    } else {
        arr = remove(arr, str);
    }

}

function addTypeVal() {
    var typeArr = [];
    var deletedArr = [];
    document.getElementsByName("type").forEach(function(element) {
    if (element.checked) {
        typeArr.push(element.value);
    } else {
        deletedArr.push(element.value);
    }
    });
    if(typeArr.length === 0){
        document.getElementById("plus-type-button").checked = false;
        alert("PLEASE SELECT A TYPE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    }
    else{
        var index;
        if(document.getElementById("plus-type-button").checked){
            for (index = 0; index < deletedArr.length; index++){
                typeArr = remove(typeArr, deletedArr[index]);
            }
            for (index = 0; index < typeArr.length; index++){
                if(!arr.includes(typeArr[index])){
                    arr.push(typeArr[index]);
                }
            }
            console.log("adding");
            console.log(typeArr);
            console.log(arr);

        }
        else{
            document.getElementsByName("type").forEach(function (element) {
                if(element.checked && typeArr.includes(element.value)){
                    element.checked = false;
                    typeArr = remove(typeArr, element.value);
                    deletedArr.push(arr, element.value);
                }
            });
            for (index = 0; index < deletedArr.length; index++){
                typeArr = remove(typeArr, deletedArr[index]);
            }

            for (index = 0; index < deletedArr.length; index++){
                arr = remove(arr, deletedArr[index]);
            }
            console.log("removing");
            console.log(typeArr);
            console.log(arr);
        }
    }
}

function addPositivesVal() {
    var posVal = document.getElementById("pos").toString();
    if (posVal !== "") {
        document.getElementsByName("positives").forEach(function(element) {
            if (element.isChecked()) {
                arr.push("positive:" + posVal + " " + element.getAttribute(value));
            } else {
                remove(arr, "positive:" + posVal + " " + element.getAttribute(value));
            }
        });
    }
}

function addChildrenPositivesVal() {
    var childrenPosVal = document.getElementById("child-pos").toString();

    if (childrenPosVal !== "") {
        document.getElementsByName("positives").forEach(function(element) {
            if (element.isChecked()) {
                arr.push("children-positive:" + childrenPosVal + " " + element.getAttribute(value));
            } else {
                remove(arr, "children-positive:" + childrenPosVal + " " + element.getAttribute(value));
            }
        });
    }
}

function addFileName() {
    var fileName = document.getElementById("file-name").toString();
    if (fileName !== "") {
        if ($("#file-name-button:checked")) {
            arr.push("file name:" + fileName);
        } else {
            remove(arr, "file name:" + fileName);
        }
    }
}

function addFSDate() {

}

function addLSDate() {

}

function addLADate() {

}

function addSourcesVal() {
    var sources = document.getElementById("sources").toString();

    if (sources !== "") {
        document.getElementsByName("sources").forEach(function(element) {
            if (element.isChecked()) {
                arr.push("sources:" + sources + " " + element.getAttribute(value));
            } else {
                remove(arr, "sources:" + sources + " " + element.getAttribute(value));
            }
        });
    }
}

function addSubmissionsVal() {
    var submissions = document.getElementById("submission").toString();

    if (submissions !== "" && document.getElementById("submission-button").isChecked()) {
        document.getElementsByName("submissions").forEach(function(element) {
            if (element.isChecked()) {
                arr.push("submission:" + submissions + " " + element.getAttribute(value));
            } else {
                remove(arr, "submission:" + submissions + " " + element.getAttribute(value));
            }
        });
    }
}

function addSubmitterVal() {
    var submitter = document.getElementById("file-name").toString();
    if (submitter !== "") {
        if ($("#submitter-button:checked")) {
            arr.push("submitter:" + submitter);
        } else {
            remove(arr, "submitter:" + submitter);
        }
    }
}

function addTaggedValues() {
    document.getElementsByName("tagged").forEach(function(element) {
        if (element.isChecked()) {
            arr.push(element.getAttribute(value));
        } else if (element.isUnchecked()) {
            remove(arr, element.getAttribute(value));
        }
    });
}

function addSectionVal() {
    var section = document.getElementById("file-name").toString();
    if (section !== "") {
        if ($("#section-button:checked")) {
            arr.push("section:" + section);
        } else {
            remove(arr, "section:" + section);
        }
    }

}

function addImportVal() {
    var imports = document.getElementById("file-name").toString();
    if (imports !== "") {
        if ($("#imports-button:checked")) {
            arr.push("imports:" + imports);
        } else {
            remove(arr, "imports:" + imports);
        }
    }
}

function addExportVal() {
    var exports = document.getElementById("file-name").toString();
    if (exports !== "") {
        if ($("#exports-button:checked")) {
            arr.push("exports:" + exports);
        } else {
            remove(arr, "exports:" + exports);
        }
    }
}

$(".plus").change(function() {
    var text = "";
    if(arr.length>0){
        for(var i = 0; i < arr.length; i++){
            text += arr[i] + " ";
        }
        $("#searchQuery").val(text);
    }
    if(arr.length === 0){
        text = "";
        $("#searchQuery").val(text);
    }

});

function add() {

}


var grd = function() {
    $("input[type='radio']").click(function() {
        var previousValue = $(this).attr('previousValue');
        var name = $(this).attr('name');

        if (previousValue === 'checked') {
            $(this).removeAttr('checked');
            $(this).attr('previousValue', false);
            $(this).prop("checked", false);
        } else {
            $("input[name=" + name + "]:radio").attr('previousValue', false);
            $(this).attr('previousValue', 'checked');
        }
    });
};
grd();