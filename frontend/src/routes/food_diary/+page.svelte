<script>
  import { Card, Button } from 'flowbite-svelte';

  let vCard = false;  // reverse 속성을 설정하는 변수
</script>

<div class="bg-zinc-50/70 flex flex-col mb-5 overflow-hidden border rounded-xl shadow-md p-4 space-y-4">
  <div class="bg-white p-4 rounded-lg shadow-md flex flex-col">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-center">닭가슴살 샐러드 파스타</h5>
      <div class="flex flex-row">
          <img src="/images/image-1.webp" alt="Image" class="rounded-lg w-1/3 h-64 object-cover" />
          <div class="flex flex-col justify-between p-4 w-2/3">
              <p class="flex mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
                  Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
              </p>
              <Button class='flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]'>
                  Read more
              </Button>
          </div>
      </div>
  </div>

  <div class="bg-white p-4 rounded-lg shadow-md flex flex-col">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white text-center">닭가슴살 샐러드 파스타</h5>
      <div class="flex flex-row">
          <img src="/images/image-1.webp" alt="Image" class="rounded-lg w-1/3 h-64 object-cover" />
          <div class="flex flex-col justify-between p-4 w-2/3">
              <p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
                  Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse chronological order.
              </p>
              <Button class = 'flex border-[1px] border-zinc-500 text-xxs font-semibold font-PoetsenOne  bg-[#E8C9D5]/50 text-zinc-950 hover:bg-[#E8C9D5]'>
                  Read more
              </Button>
          </div>
          
      </div>
  </div>
</div>
