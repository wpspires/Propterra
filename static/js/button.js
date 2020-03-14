$(function () {
    $("#btnCalculate").on("click", function ()
    {
        var input = $('#txtLocationInput').val();
        console.log(input);
        $.post(URL="./calculate", { "address" : input })

    });
});

function onSuccess()
{
    console.log("yay");
}