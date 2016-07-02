function grillmon() {
    parseTemp = function(temp) {
        //console.log(temp);
        this.postUI = false;
        try {
            if (temp["fault"]) {
                $("#thermo-fault").text(temp["fault"]);
            } else {
                $("#thermo-fault").text(temp[""]);
            }
            if (temp["externalF"]) {
                $("#thermo-externalF").html(temp["externalF"] + " &deg; F");
            } else {
                $("#thermo-externalF").html("");
            }
            if (temp["internalF"]) {
                $("#thermo-internalF").html(temp["internalF"] + " &deg; F");
            } else {
                $("#thermo-internalF").html("");
            }
        }
        finally {
            this.postUI = true;
        }
    }

    requestTemp = function() {
        $.ajax({
            url: "/grillmon/getTemp",
            dataType : 'json',
            type : 'GET',
            success: function(newData) {
                $("#error-box").hide();
                grillmon.parseTemp(newData);
                setTimeout("grillmon.requestTemp();", 1000);
            },
            error: function() {
                console.log("error retrieving settings");
                setTimeout("grillmon.requestTemp();", 5000);
                $("#error-message").text("error retrieving settings");
                $("#error-box").show();
            }
        });
    }

    start = function() {
         this.postUI = true;
         //this.initButtons();
         this.requestTemp();
    }

    return this;
}

$(document).ready(function(){
    grillmon = grillmon()
    grillmon.start();
});

