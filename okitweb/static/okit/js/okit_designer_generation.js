console.log('Loaded Generation Javascript');

/*
** Generate Button handlers
 */

function openInNewTab(url) {
    let win = window.open(url, '_blank');
    win.focus();
}

function handleGenerateTerraform(e) {
    hideNavMenu();
    $.ajax({
        type: 'post',
        url: 'generate/terraform',
        dataType: 'text',
        contentType: 'application/json',
        data: JSON.stringify(OKITJsonObj),
        success: function(resp) {
            console.log('Response : ' + resp);
            window.location = 'generate/terraform';
            //openInNewTab('generate/terraform');
        },
        error: function(xhr, status, error) {
            console.log('Status : '+ status)
            console.log('Error : '+ error)
        }
    });
}

function handleGenerateAnsible(e) {
    hideNavMenu();
    $.ajax({
        type: 'post',
        url: 'generate/ansible',
        dataType: 'text',
        contentType: 'application/json',
        data: JSON.stringify(OKITJsonObj),
        success: function(resp) {
            console.log('REST Response : ' + resp);
            window.location = 'generate/ansible';
            //openInNewTab('generate/ansible');
        },
        error: function(xhr, status, error) {
            console.log('Status : '+ status)
            console.log('Error : '+ error)
        }
    });
}

function handleGenerateTerraform11(e) {
    hideNavMenu();
    $.ajax({
        type: 'post',
        url: 'generate/terraform11',
        dataType: 'text',
        contentType: 'application/json',
        data: JSON.stringify(OKITJsonObj),
        success: function(resp) {
            console.log('Response : ' + resp);
            window.location = 'generate/terraform11';
        },
        error: function(xhr, status, error) {
            console.log('Status : '+ status)
            console.log('Error : '+ error)
        }
    });
}

function handleExportToResourceManager(e) {
    hideNavMenu();
    $.ajax({
        type: 'post',
        url: 'export/resourcemanager',
        dataType: 'text',
        contentType: 'application/json',
        data: JSON.stringify(OKITJsonObj),
        success: function(resp) {
            console.log('Response : ' + resp);
            alert('Created Stack ' + resp);
            //window.location = 'generate/terraform';
            //openInNewTab('generate/terraform');
        },
        error: function(xhr, status, error) {
            console.log('Status : '+ status)
            console.log('Error : '+ error)
        }
    });
}

