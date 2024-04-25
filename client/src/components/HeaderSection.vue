<template>
   <div class="container">
      <div class="row justify-content-center align-items-center text-center">
        <div class="col-12 my-2">
          <h1 class="heeading-1">My Book Store</h1>
          <h2 class="h4 text-white">
            if you want to add new books you can click to button.
          </h2>
        </div>
        <div class="col-6 my-2">
          <button
            type="button"
            class="btn btn-success"
            data-bs-toggle="modal"
            data-bs-target="#exampleModal"
          >
            Add Book
          </button>
          <div
            class="modal fade"
            id="exampleModal"
            tabindex="-1"
            aria-labelledby="exampleModalLabel"
            aria-hidden="true"
          >
            <div class="modal-dialog modal-dialog-centered modal-lg">
              <div class="modal-content modal-content-horizontal">
                <div class="modal-header">
                  <h1 class="modal-title fs-5"  id="exampleModalLabel">
                    Please Paste Book Link
                  </h1>
                  <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                  ></button>
                </div>
                <div class="modal-body">
                  <div class="input-group">
                    <div class="input-group-prepend">
                      <div class="input-group-text">
                        {{ url }}
                      </div>
                    </div>
                    <input
                      type="text"
                      class="form-control"
                      id="inlineFormInputGroupUsername"
                      placeholder="book link"
                      :value="link"
                      @input="$emit('update:link', $event.target.value)"
                    />
                    <button class="btn btn-success"  @click="sendForm">
                      Add
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  name:'HeaderSection',
  props:{
    url:String,
    sendForm:String,
    link:String,
    
    
  },

}
</script>