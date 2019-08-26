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

    if (sizeVal !== "" || (typeof sizeType === 'undefined' || typeof sizeMag === 'undefined')) {
        sizeType = $('input[name=size-val]:checked').val();
        sizeMag = $('input[name=size-mag]:checked').val();
    }

    var str = "size:" + sizeVal + " " + sizeType + " " + sizeMag;
    if (document.getElementById("plus-size-button").checked) {
        arr.push(str);
    } else {
        document.getElementsByName("size-val").forEach(
            function (element) {
                element.checked = false;
            }
        );

        document.getElementsByName("size-mag").forEach(
            function (element) {
                element.checked = false;
            }
        );
        document.getElementById("size").value = "";
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
        }
    }
}

function addPositivesVal() {
    var posVal = document.getElementById("positives").value;
    var str = "";
    var posMag = "";
    document.getElementsByName("positives").forEach(function(element) {
        if (element.checked) {
            posMag = element.value;
        }
    });
    str = "positive:" + posVal + " " + posMag;
    if(document.getElementById("plus-positives-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("positives").forEach(function (element) {
            element.checked = false;
        });
        document.getElementById("positives").value = "";
    }

}

function addChildrenPositivesVal() {
    var posVal = document.getElementById("children-positives").value;
    var str;
    var posMag = "";
    document.getElementsByName("children-positives").forEach(function(element) {
        if (element.checked) {
            posMag = element.value;
        }
    });
    str = "children-positive:" + posVal + " " + posMag;
    if(document.getElementById("plus-children-pos-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("children-positives").forEach(function (element) {
            element.checked = false;
        });
        document.getElementById("children-positives").value = "";
    }
}

function addFileName() {
    var fileName = document.getElementById("file-name");

    if (fileName.value !== "") {
        var str = "file name:" + fileName.value;
    }
    if(document.getElementById("plus-file-name-button").checked){
        arr.push(str);
    }
    else{
        arr = remove(arr, str);
        fileName.value = "";
    }
}

function addSourcesVal() {
    var sources = document.getElementById("sources").value;
    var str;
    var sourceMag = "";
    document.getElementsByName("sources").forEach(function(element) {
        if (element.checked) {
            sourceMag = element.value;
        }
    });
    str = "sources:" + sources + " " + sourceMag;

    if(document.getElementById("plus-sources-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("sources").forEach(function (element) {
            element.checked = false;
        });
        document.getElementById("sources").value = "";
    }

}

function addSubmissionsVal() {
    var submissions = document.getElementById("submission").value;
    var str;
    var subMag = "";
    document.getElementsByName("submissions").forEach(function(element) {
        if (element.checked) {
            subMag = element.value;
        }
    });
    str = "submissions:" + submissions + " " + subMag;

    if(document.getElementById("plus-submissions-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("submissions").forEach(function (element) {
            element.checked = false;
        });
        document.getElementById("submission").value = "";
    }
}

function addSubmitterVal() {
    var submitter = document.getElementById("submitter");

    if (submitter.value !== "") {
        var str = "submitter:" + submitter.value;
    }
    if(document.getElementById("plus-submitter-button").checked){
        arr.push(str);
    }
    else{
        arr = remove(arr, str);
        submitter.value = "";
    }
}

function addTaggedValues() {
    var taggedArr = [];
    var deletedArr = [];
    document.getElementsByName("tagged").forEach(function(element) {
    if (element.checked) {
        taggedArr.push(element.value);
    } else {
        deletedArr.push(element.value);
    }
    });
    if(taggedArr.length === 0){
        document.getElementById("plus-tagged-button").checked = false;
        alert("PLEASE SELECT A TYPE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    }
    else{
        var index;
        if(document.getElementById("plus-tagged-button").checked){
            for (index = 0; index < deletedArr.length; index++){
                taggedArr = remove(taggedArr, deletedArr[index]);
            }
            for (index = 0; index < taggedArr.length; index++){
                if(!arr.includes(taggedArr[index])){
                    arr.push(taggedArr[index]);
                }
            }
        }
        else{
            document.getElementsByName("tagged").forEach(function (element) {
                if(element.checked && taggedArr.includes(element.value)){
                    element.checked = false;
                    taggedArr = remove(taggedArr, element.value);
                    deletedArr.push(arr, element.value);
                }
            });
            for (index = 0; index < deletedArr.length; index++){
                taggedArr = remove(taggedArr, deletedArr[index]);
            }

            for (index = 0; index < deletedArr.length; index++){
                arr = remove(arr, deletedArr[index]);
            }
        }
    }
}

function addSectionVal() {
    var section = document.getElementById("section");

    if (section.value !== "") {
        var str = "section:" + section.value;
    }
    if(document.getElementById("plus-section-button").checked){
        arr.push(str);
    }
    else{
        arr = remove(arr, str);
        section.value = "";
    }

}

function addImportVal() {
    var imports = document.getElementById("imports");

    if (imports.value !== "") {
        var str = "imports:" + imports.value;
    }
    if(document.getElementById("plus-imports-button").checked){
        arr.push(str);
    }
    else{
        arr = remove(arr, str);
        imports.value = "";
    }
}

function addExportVal() {
    var exports = document.getElementById("exports");

    if (exports.value !== "") {
        var str = "exports:" + exports.value;
    }
    if(document.getElementById("plus-exports-button").checked){
        arr.push(str);
    }
    else{
        arr = remove(arr, str);
        exports.value = "";
    }
}

function addFirstSubmissionDate(){
    var date = document.getElementById("first-submission-date");
    var str;
    if (date.value !== "") {
        str = "first submission date:" + date.value;
    }
    var dateMag = "";
    document.getElementsByName("fsd").forEach(function(element) {
        if (element.checked) {
            dateMag = element.value;
        }
    });
    str +=" " + dateMag;
    if(document.getElementById("plus-first-submission-date-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("fsd").forEach(function (element) {
            element.checked = false;
        });
        date.value = "";
    }
}

function addLastSubmissionDate(){
    var date = document.getElementById("last-submission-date");
    var str;
    if (date.value !== "") {
        str = "last submission date:" + date.value;
    }
    var dateMag = "";
    document.getElementsByName("lsd").forEach(function(element) {
        if (element.checked) {
            dateMag = element.value;
        }
    });
    str +=" " + dateMag;
    if(document.getElementById("plus-last-submission-date-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("lsd").forEach(function (element) {
            element.checked = false;
        });
        date.value = "";
    }
}

function addLastAnalysisDate(){
    var date = document.getElementById("last-analysis-date");
    var str;
    if (date.value !== "") {
        str = "last analysis date:" + date.value;
    }
    var dateMag = "";
    document.getElementsByName("lad").forEach(function(element) {
        if (element.checked) {
            dateMag = element.value;
        }
    });
    str +=" " + dateMag;
    if(document.getElementById("plus-last-analysis-date-button").checked){
        arr.push(str);
    }
    else{
        if (arr.includes(str)){
            console.log(str);
            arr = remove(arr, str);
        }
        document.getElementsByName("lad").forEach(function (element) {
            element.checked = false;
        });
        date.value = "";
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