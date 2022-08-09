const IMP = window.IMP;
const merchant_uid = IMP.init("imp74307179");

function requestPay() {
    // IMP.request_pay(param, callback) 결제창 호출
    IMP.request_pay({ // param
        pg: "kakaopay",
        pay_method: "kakaopay",
        merchant_uid: "ORD20180131-0000012",
        name: "아이폰11",
        amount: 1900,
        buyer_email: "gildong@gmail.com",
        buyer_name: "홍길동",
        buyer_tel: "010-4242-4242",
        buyer_addr: "서울특별시 강남구 신사동",
        buyer_postcode: "01181"
    }, function (rsp) { // callback
        if (rsp.success) {
            // jQuery로 HTTP 요청
            jQuery.ajax({
                url: "127.0.0.1:8000/onedeal/create", // 예: https://www.myservice.com/payments/complete
                method: "POST",
                headers: {"Content-Type": "application/json"},
                data: {
                    imp_uid: rsp.imp_uid,
                    merchant_uid: rsp.merchant_uid
                }
            }).done(function (data) {
                // 가맹점 서버 결제 API 성공시 로직
            })
        } else {
            alert("결제에 실패하였습니다. 에러 내용: " + rsp.error_msg);
        }
    });
}