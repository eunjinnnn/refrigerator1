<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-green-700 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<Navbar class="bg-orange-50  border-b-2 border-lime-950">
  <NavBrand href="/">
    <span class="self-center font-serif whitespace-nowrap text-lime-950 text-lg font-semibold">My Refrigerator</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass} >
    <NavLi href="/" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">HOME</NavLi>
    <NavLi href="/add" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">ADD</NavLi>
    <NavLi href="/delete" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">DELETE</NavLi>
    <NavLi href="/my_refrigerator" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">MY REFRIGERATOR</NavLi>
    <NavLi href="/food_diary" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">FOOD DIARY</NavLi>
    <NavLi href="/receipe" size="sm" class="text-sm border-b-2 border-transparent hover:border-gray-500">RECEIPE</NavLi>
  </NavUl>
</Navbar>


<div class="py-2 sm:py-4 px-2 sm:px-4">
    <div class="container mx-auto">
        <slot></slot>
    </div>
</div>
