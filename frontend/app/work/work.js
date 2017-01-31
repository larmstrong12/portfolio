'use strict';

angular.module('myApp.work', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/work', {
            templateUrl: 'work/work.html',
            controller: 'WorkCtrl'
        });
    }])

    .controller('WorkCtrl', ['$scope', 'Restangular', function ($scope, Restangular) {
        $scope.pricing = {
            option: []
        };

        $scope.addRequest = function () {
            Restangular.all('add-request').customPOST($scope.request).then(function () {
                toastr.success("You successfully sent the request!");
                $scope.$apply();
                $scope.pricing = {option: []};
            }, function () {
                toastr.error("There was a problem sending your request. Please contact me directly at " +
                    "lyndseearmstrong@gmail.com");
            });
        };
    }]);