'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
    'ngRoute',
    'myApp.recipes',
    'myApp.recipeDetail',
    'myApp.addRecipe',
    'myApp.contact',
    'myApp.home',
    'myApp.blog',
    'myApp.work',
    'myApp.version',
    'restangular'
]).
    config(['$routeProvider', 'RestangularProvider', function ($routeProvider, RestangularProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});

        RestangularProvider.setBaseUrl('/app');
        RestangularProvider.setRequestSuffix('/');
    }]);
