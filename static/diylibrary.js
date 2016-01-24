function replaceUrlParam(url, paramName, paramValue){
    var pattern = new RegExp('\\b('+paramName+'=).*?(&|$)')
    if(url.search(pattern)>=0){
        return url.replace(pattern,'$1' + paramValue + '$2');
    }
    return url + (url.indexOf('?')>0 ? '&' : '?') + paramName + '=' + paramValue
}

function capitalize(token) {
    return token.charAt(0).toUpperCase() + token.slice(1);
}

var app = angular.module('diylibraryApp', ['ngAnimate', 'ngTouch', 'ui.grid',  'ui.grid.selection']);

app.config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('{[');
    $interpolateProvider.endSymbol(']}');
}]);

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.factory('data', function () {
    return {
        'bookq': {},
        'readersGridApi': null
    };
});

app.controller('ReadersCtrl', function($scope, $http, $interval, data) {
    $scope.readers = {
        multiSelect: false,
        enableFiltering: true,
        enableRowSelection: true,
        enableRowHeaderSelection: false,
        data: [],
        columnDefs: [
            { name: 'id', visible: false},
            { name: 'name'},
        ],
        onRegisterApi: function(gridApi) {
            $scope.readersGridApi = gridApi;
            data['readersGridApi'] = gridApi;
            console.log($scope.readersGridApi);
            console.log($scope);

            $http.get('/api/reader/all').then(function(response) {
                $scope.readers.data = response.data.readers;
            });
        }
    };

    $scope.book_reserve = function() {
        var book_id = data.selectedBook;
        var sel = $scope.readersGridApi.selection.getSelectedRows();
        if (sel.length > 0) {
            var reader_id = sel[0].id;
            $('#book-reserve-modal').modal('hide');
            $http.post('/api/book/reserve/?id='+ book_id + '&reader_id=' + reader_id).then(function() {
                data['bookq'][book_id] -= 1;
            });
        } else {
            alert('Необходимо выбрать читателя');
        }
    }

    $scope.new_reader_show = function() {
        $('#book-reserve-modal').modal('hide');
        $('#new-reader-modal').modal('show');
    };

    $scope.new_reader = function() {
        var postData = {
            name: $scope.newReader.name,
            phone: $scope.newReader.phone,
            email: $scope.newReader.email
        };
        $http.post('/api/reader/new', postData).then(function(response) {
            if (response.data.error) {
                alert(response.data.error);
            } else {
                $scope.newReader.name = '';
                $scope.newReader.phone = '';
                $scope.newReader.email = '';

                $scope.readers.data.unshift(response.data);
                var book_id = data.selectedBook;
                var reader_id = response.data.id;
                $('#new-reader-modal').modal('hide');
                $http.post('/api/book/reserve/?id='+ book_id + '&reader_id=' + reader_id).then(function() {
                    data['bookq'][book_id] -= 1;
                });
            }
        });
    }

});

app.controller('BooksCtrl', function($scope, $http, $interval, data) {
    $scope.bookq = data['bookq'];
    $scope.book_reserve_show = function(book_id) {
        $('#book-reserve-modal').modal('show');
        data['readersGridApi'].core.refresh();
        data['readersGridApi'].core.handleWindowResize();
        data.selectedBook = book_id;
        return false;
    }

});

app.controller('ReadingCtrl', function($scope, $location) {
    $('#show_returned').change(function() {
        var url = replaceUrlParam(
            window.location.href,
            'show_returned',
            $('#show_returned').is(':checked')
        );
        window.location = url;
    });
});

function update_quantity(book_id, url) {
    $.ajax({url: url, dataType: 'json'}).success(
        function(data) {
            $('#book-' + book_id).find('.is-quantity').html(data.quantity);
            $('#book-' + book_id).find('.is-quantity-total').html(data.quantity_total);
            console.log($('#book-' + book_id).find('.is-quantity'));
        }
    );
}

function reading_return(reading_id) {
    var button = $('#reading-return-btn-' + reading_id);
    if (confirm(button.attr('confirm-msg'))) {
        $.ajax({url: '/api/reading/return?id=' + reading_id, dataType: 'json'}).success(
            function(data) {
                if(data.error) {
                    alert(data.error);
                } else {
                    $('#reading-date-' + reading_id).html(data.returned_at);
                    button.hide();
                    $('#reading-undo-btn-' + reading_id).show();
                }
            }
        );
    }
    return false;
}

function reading_undo(reading_id) {
    var button = $('#reading-undo-btn-' + reading_id);
    if (confirm(button.attr('confirm-msg'))) {
        $.ajax({url: '/api/reading/undo?id=' + reading_id, dataType: 'json'}).success(
            function(data) {
                if(data.error) {
                    alert(data.error);
                } else {
                    $('#reading-date-' + reading_id).html('');
                    button.hide();
                    $('#reading-return-btn-' + reading_id).show();
                }
            }
        );
    }
    return false;
}
