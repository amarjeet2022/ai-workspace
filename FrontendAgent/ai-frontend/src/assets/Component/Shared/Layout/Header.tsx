 const Header = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-4 flex items-center justify-between">
        <h1 className="text-xl font-bold">My Application</h1>
        <nav>
          <ul className="flex space-x-4">
            <li><a href="/" className="text-gray-700 hover:text-gray-900">Home</a></li>
            <li><a href="/about" className="text-gray-700 hover:text-gray-900">About</a></li>
            <li><a href="/contact" className="text-gray-700 hover:text-gray-900">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
};

export default Header;