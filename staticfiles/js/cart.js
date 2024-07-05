var updateBtns = document.getElementsByClassName('update-cart')


for (var i=0; i<updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var courseId = this.dataset.course
        var action = this.dataset.action
        console.log('courseId:',courseId, 'action:',action)
        console.log("Cart")
    })
}