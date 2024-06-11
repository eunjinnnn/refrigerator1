<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-green-700 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<Navbar class="fixed top-0 left-0 w-full z-50 bg-orange-50/60 flex items-center justify-between px-4 py-2 shadow-md border-b border-gray-300">
  <NavBrand href="/">
    <!-- <img src="/images/FRESHKEEP.png" class="h-8 sm:h-6 md:h-4 lg:h-3 xl:h-2 mt-2 max-w-full" alt="FreshKeep Logo" /> -->
    <h1 class="text-3xl sm:text-xl font-grandstander font-semibold text-amber-950 mt-2">FRESHKEEP</h1>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass} class="flex items-center space-x-4">
    <NavLi href="/my_refrigerator" class="font-PoetsenOne text-lime-950 hover:text-orange-50 transition-colors duration-300">MY REFRIGERATOR</NavLi>
    <NavLi href="/food_diary" class="font-PoetsenOne text-lime-950 hover:text-orange-50 transition-colors duration-300">FOOD DIARY</NavLi>
    <NavLi href="/receipe" class="font-PoetsenOne text-lime-950 hover:text-orange-50 transition-colors duration-300">RECEIPE</NavLi>
  </NavUl>
</Navbar>

<!-- stone-200 -->
<div class="min-h-screen bg-cover bg-center" style="background-image: url('/images/bg1.jpg');">
  <div class="min-h-80 p-2 sm:p-4">
      <div class="flex flex-col">
        <div class="mt-16 px-3">
          <slot></slot>
        </div>
      </div>
  </div>
</div>

<style>
  .bg-cover {
    background-size: cover;
  }
  .bg-center {
    background-position: center;
  }
</style>
