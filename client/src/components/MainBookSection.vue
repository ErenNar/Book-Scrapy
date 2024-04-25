<template>
  <section v-if="loading == true">
    <div class="loading-container">
      <div class="loader"></div>
    </div>
  </section>
  <section v-else>
    <div class="container py-5">
      <div class="row justify-content-start align-items-center">
        <h1 class="h1" style="color: #703804">Related Books</h1>
        <hr style="border: 5px solid #703804" />
      </div>
      <div class="row justify-content-start align-items-center">
        <div
          class="col-10 col-md-4 col-lg-3"
          v-for="(item, key1) in filterDataBook"
          :key="key1"
        >
          <div
            type="button"
            data-bs-toggle="modal"
            :data-bs-target="'#book-detal-' + key1"
          >
            <div class="card">
              <div class="card-body">
                <div class="bookWrap">
                  <div class="book">
                    <img
                      class="cover"
                      :src="
                        'https://i.dr.com.tr/cache/500x400-0/originals/' +
                        item.book_img
                      "
                    />
                    <div class="spine"></div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="modal fade"
              :id="'book-detal-' + key1"
              tabindex="-1"
              :aria-labelledby="'book-detal-' + key1"
              aria-hidden="true"
            >
              <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content modal-content-par">
                  <div class="modal-header py-5">
                    <div class="row d-flex align-items-center">
                      <div class="col-auto">
                        <h1 class="modal-title fs-5" :id="'book-detal-' + key1">
                          <a
                            :href="item.url"
                            target="_blank"
                            style="color: black; font-weight: 700"
                          >
                            {{ item.book_title }}
                          </a>
                        </h1>
                      </div>
                      <div class="col-auto">
                        <span class="badge text-bg-info rounded-pill">{{
                          item.book_price
                        }}</span>
                      </div>
                    </div>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                  </div>
                  <div class="modal-body py-5 px-5">
                    <div class="row">
                      <div class="col-auto">
                        <img
                          :src="
                            'https://i.dr.com.tr/cache/500x400-0/originals/' +
                            item.book_img
                          "
                          alt=""
                        />
                      </div>
                      <div
                        class="col-12 col-lg-7"
                        v-html="item.book_features"
                      ></div>
                      <div
                        class="col-12 my-2"
                        v-html="item.product_description"
                      ></div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <a
                      class="btn btn-danger"
                      @click="deleteProduct(item._id.$oid)"
                    >
                      <img src="./assets/image/delete.png" width="20" alt="" />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container py-5">
      <div class="row justify-content-start align-items-center">
        <h1 class="h1" style="color: #703804">Other Books</h1>
        <hr style="border: 5px solid #703804" />
      </div>
      <div class="row justify-content-center justify-content-lg-start">
        <div
          class="col-10 col-md-3 col-lg-2 mx-5 my-3"
          v-for="(item, key2) in dataBook"
          :key="key2"
        >
          <div
            type="button"
            data-bs-toggle="modal"
            :data-bs-target="'#book-detall-' + key2"
          >
            <div class="card">
              <div class="card-body">
                <div class="panel__image panel__image--book">
                  <a href="#" class="books__book__image">
                    <div class="books__book__img">
                      <img
                        :src="
                          'https://i.dr.com.tr/cache/500x400-0/originals/' +
                          item.book_img
                        "
                      />
                    </div>
                  </a>
                </div>
              </div>
            </div>
            <div
              class="modal fade"
              :id="'book-detall-' + key2"
              tabindex="-1"
              :aria-labelledby="'book-detall-' + key2"
              aria-hidden="true"
            >
              <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content modal-content-par">
                  <div class="modal-header py-5">
                    <div class="row align-items-center justify-content-between">
                      <div class="col-auto">
                        <a
                          :href="item.url"
                          target="_blank"
                          style="font-weight: 700; color: black"
                        >
                          <h1
                            class="modal-title fs-5"
                            :id="'book-detall-' + key2"
                          >
                            {{ item.book_title }}
                          </h1>
                        </a>
                      </div>
                      <div class="col-auto">
                        <span class="badge text-bg-info rounded-pill">{{
                          item.book_price
                        }}</span>
                      </div>
                    </div>

                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                  </div>
                  <div class="modal-body py-5 px-5">
                    <div class="row">
                      <div class="col-auto">
                        <img
                          :src="
                            'https://i.dr.com.tr/cache/500x400-0/originals/' +
                            item.book_img
                          "
                          alt=""
                        />
                      </div>
                      <div
                        class="col-12 col-lg-7"
                        v-html="item.book_features"
                      ></div>
                      <div
                        class="col-12 my-2"
                        v-html="item.product_description"
                      ></div>
                    </div>
                  </div>
                  <div class="modal-footer">
                    <a
                      class="btn btn-danger"
                      href=""
                      @click="deleteProduct(item._id.$oid)"
                    >
                      <img src="../assets/image/delete.png" width="20" alt="" />
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "MainBookSection",

  props: {
    loading: Boolean,
    filterDataBook: Array,
    dataBook:Array,
    deleteProduct:String
  },
};
</script>
