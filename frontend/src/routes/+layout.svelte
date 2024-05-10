<script>
  import { page } from '$app/stores';
  import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
  $: activeUrl = $page.url.pathname;
  let activeClass = 'text-white bg-green-700 md:bg-transparent md:text-green-700 md:dark:text-white dark:bg-green-600 md:dark:bg-transparent';
  let nonActiveClass = 'text-gray-700 hover:bg-gray-100 md:hover:bg-transparent md:border-0 md:hover:text-green-700 dark:text-gray-400 md:dark:hover:text-white dark:hover:bg-gray-700 dark:hover:text-white md:dark:hover:bg-transparent';
</script>

<Navbar let:NavContainer color="green" >
  <NavBrand href="/">
    <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white" style='font-size:small'>REFRIGERATOR</span>
  </NavBrand>
  <NavHamburger />
  <NavUl {activeUrl} {activeClass} {nonActiveClass}>
    <NavLi href="/" size = 'sm' class='text-sm'>HOME</NavLi>
    <NavLi href="/add" size = 'sm' class='text-sm'>ADD</NavLi>
    <NavLi href="/delete" size = 'sm' class='text-sm'>DELETE</NavLi>
    <NavLi href="/my_refrigerator" size = 'sm' class='text-sm'>MY REFRIGERATOR</NavLi>
    <NavLi href="/food_diary" size = 'sm' class='text-sm'>FOOD DIARY</NavLi>
    <NavLi href="/receipe" size = 'sm' class='text-sm'>RECEIPE</NavLi>
  </NavUl>
</Navbar>

<div class="px-2 sm:px-4">
    <div class="container mx-auto">
        <slot></slot>
    </div>
</div>
