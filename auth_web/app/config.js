﻿var baseUrl = 'http://localhost:9000/';
var loginUrl = 'http://localhost:9001/auth_web/';
var iotecaUrl = 'http://localhost:9001/redcashier_web/';


<<<<<<< HEAD
<<<<<<< HEAD
var clientId = '3XKkPgFcteHXNKKUMt0o5Ej3Qg5Cb6i5N5IXLyUZ';
var clientSecret = 'nD6H6YqjD5TXD3E33IbhJgredn1tJASx33oUfkbb3LXuovXhKCxFIBmJAjHwjE0atlsPj3EE3qbLI3ffoSOWoTftXCoLjZm54Gbl1r9QDSgvpAiYNUGcxMcMqZqAGE0V';
=======
var clientId = 'EF1hlZ2KiPu97nAukLFCQLbSfm3dKvA5qQEfufn5';
var clientSecret = 'G9BdLe5zLh3gXaeTW6yhdzyjQPHFKEVLXTn4sJSAUYC1JD2Tu1MfYATkkqFvzmgoo2WRAlJ6h8nRQEcAPcxjNevz3A3b1XNCCjfYDD36ZSc8fgqKHzvteWNYnBZbnB8f';
>>>>>>> 8ca5d9d1b554e7dc56beab57b192995165ada4c0
=======
var clientId = 'dKR0xatU8SYCp8DiSrs51vPJ9YB8fNOpZSN5q8nR';
var clientSecret = 'FNeFHU6SI7KKtMuAIwoAwG08uv587HARhgK6OGeXG8qxHODmn5ezaxTSsGXeDfCB5OO2Sjyco6laGgmLYnLRNe01xsgNZobHt54bPoreBavKxXdlKsPvV63zNZaiY3fY';
>>>>>>> 43184a8c69e03ecd0de6ede1e96e86ad34ad42e4
var grantType = 'password';

var config = {

    baseUrl: baseUrl,
    loginUrl: loginUrl,
    iotecaUrl: iotecaUrl,

    clientId: clientId,
    clientSecret: clientSecret,
    grantType: grantType,

};

app.value('config', config);

app
    .run(function($rootScope, $state, $stateParams, $window, loginService) {
        // It's very handy to add references to $state and $stateParams to the $rootScope
        // so that you can access them from any scope within your applications.For example,
        // <li ng-class="{ active: $state.includes('contacts.list') }"> will set the <li>
        // to active whenever 'contacts.list' or one of its decendents is active.
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;

        /*******************************agregado**************************/
        console.log("run");

        if (loginService.authentication.isAuth === false) {
            $window.location = loginUrl;
        }
        /******************************************************************/

    })

.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    //$httpProvider.interceptors.push('authInterceptorService');
})

.config(function($resourceProvider) {
    // Don't strip trailing slashes from calculated URLs
    $resourceProvider.defaults.stripTrailingSlashes = false;
});
