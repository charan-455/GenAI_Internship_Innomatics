document.getElementById('myForm').addEventListener('submit', function() {
    setTimeout(function() {
        document.getElementById('test_string').value = '';
        document.getElementById('regex_pattern').value = '';
        document.getElementById('case_insensitive').checked = false;
    }, 100);
});